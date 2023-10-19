'''Convert CSV schema files to JSON Schema'''

import csv
import io
import json
import os
import re
import requests
import dotenv
# import sys
# from genson import SchemaBuilder


def get_csv_as_dict(file_path: str, remote: bool=True) -> list:
    '''Returns a list of rows (dicts) from an input local CSV filepath or remote CSV URL'''
    rows = []

    if remote is False:
        with open(file_path, encoding='utf-8', mode = 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                rows.append(row)

    else:
        response = requests.get(file_path)
        if response.status_code == 200:
            buffer = io.StringIO(response.text)
            reader = csv.DictReader(buffer, delimiter=',', quotechar='"')
            for row in reader:
                rows.append(row)
        else:
            print(f'Check URL - {file_path} returned error: {response.status_code}')

    return rows


def validate_csv(csv_import: list, config: dict, csv_name: str):
    '''Check if required column-names exist in input-csv's'''

    column_names = csv_import[0].keys()

    required_terms = {
        config['TERM_CSV']: [
            'definition',
            'label',
            'rdf_type',
            'tdwgutility_required',
            'tdwgutility_organizedInClass',
            'term_localName'
        ],

        config['CLASS_CSV']: [
            'display_comments',
            'display_label'
        ],

        config['DATATYPES_CSV']: [
            'datatype',
            'tdwgutility_organizedInClass',
            'term_localName'
        ]
    }

    if all(check in column_names for check in required_terms[csv_name]) is False:
        missing = [x for x in required_terms[csv_name] if x not in column_names]
        print(f'{csv_name} INVALID -- missing required columns: {missing}')
        return False

    print(f'{csv_name} valid -- required columns all present')
    return True


def get_class_list(term_list: list) -> list:
    '''Get unique list of Classes defined in Latimer Core'''

    class_list = []

    for term in term_list:
        if 'tdwgutility_organizedInClass' in term:
            class_name = term['tdwgutility_organizedInClass']
            if class_name not in class_list:
                class_list.append(class_name)

    return class_list


def prep_class_name(class_name):
    '''convert CamelCase class name to kebab-case name'''

    class_name_prepped = re.sub(r'^has([A-Z].+)', r'\1', class_name)
    class_name_prepped = re.sub(r'([A-Z])', r'-\1', class_name_prepped)
    class_name_prepped = re.sub(r'^\-|\s+', '', class_name_prepped.lower())

    return class_name_prepped


def convert_csv_to_json(
    json_prefix: str,
    rows: list,
    class_row: dict,
    datatypes: list
    ) -> dict:
    '''convert each csv-column to corresponding json-schema attribute'''

    class_name_prepped = prep_class_name(class_row['display_label'])

    class_skeleton = {
        '$schema': 'https://json-schema.org/draft-04/schema',
        '$id': f'{json_prefix}/{class_name_prepped}.json',
        'title': class_row['display_label'],
        'description': class_row['display_comments'],
        'type': 'object',
        'properties': {}
    }

    required_terms = []

    for term_row in rows:
        if term_row['rdf_type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property':

            term_class_prepped = prep_class_name(term_row['tdwgutility_organizedInClass'])

            if term_class_prepped == class_name_prepped:

                term_name = term_row['term_localName']

                class_skeleton['properties'][term_name] = {
                    'description': term_row['definition'],
                    'type': None
                }

                # Add term's datatype
                for datatype in datatypes:
                    datatype_class = datatype['tdwgutility_organizedInClass']

                    term_class = term_row['tdwgutility_organizedInClass']
                    if datatype_class == term_class:
                        if datatype['term_localName'] == term_row['term_localName']:
                            class_skeleton['properties'][term_name]['type'] = datatype['datatype']


                # Add array-properties for array-terms
                if class_skeleton['properties'][term_name]['type'] == 'array':
                    term_name_prepped = prep_class_name(term_name)

                    if re.match(r'^has[A-Z].*', term_name) is not None:
                        # Handle repeatable LtC Classes (e.g. "ltc:hasIdentifier")
                        array_items = {
                            '$ref': f'{json_prefix}/{term_name_prepped}.json'
                        }

                    else:
                        # Handle repeatable LtC Terms (e.g. "ltc:alternativeCollectionName")
                        array_items = {
                            'description': term_row['definition'],
                            'type': 'string' # NOTE - defaulting to string until 'datatype' CSV indicates type within array
                        }

                    class_skeleton['properties'][term_name]['items'] = array_items
                    class_skeleton['properties'][term_name]['minItems'] = 0

                    # Check if array-term is required
                    # TODO - should this also check 'required' in CLASS csv?
                    if term_row['tdwgutility_required'] == 'Yes':
                        class_skeleton['properties'][term_name]['minItems'] = 1
                    class_skeleton['properties'][term_name]['uniqueItems'] = True

                # Check if term is required
                if term_row['tdwgutility_required'] == 'Yes':
                    required_terms.append(term_row['term_localName'])

    if len(required_terms) > 0:
        class_skeleton['required'] = required_terms

    return class_skeleton


def main():
    '''main script'''

    # Get env variables/input
    config = dotenv.dotenv_values(".env")
    uri_raw_prefix = config['URI_RAW_PREFIX']
    repo_branch = config['REPO_BRANCH']
    repo_csv_path = config['REPO_PATH_TO_CSV']
    repo_json_path = config['REPO_PATH_TO_JSON']

    class_csv = config['CLASS_CSV']
    term_csv = config['TERM_CSV']
    datatypes_csv = config['DATATYPES_CSV']
    # skos_csv = config['SKOS_CSV']

    json_output_path = config['JSON_OUTPUT_PATH']

    csv_prefix = f'{uri_raw_prefix}/{repo_branch}/{repo_csv_path}'
    json_prefix = f'{uri_raw_prefix}/{repo_branch}/{repo_json_path}'


    # Import CSVs

    # # import terms
    terms_csv_file = f'{csv_prefix}/{term_csv}'
    term_list = get_csv_as_dict(file_path=terms_csv_file)
    term_list = sorted(term_list, key = lambda i:i['term_localName'])

    # # import class list
    class_csv_file = f'{csv_prefix}/{class_csv}'
    class_list = get_csv_as_dict(file_path=class_csv_file)

    # # import datatypes
    datatype_csv_file = f'{csv_prefix}/{datatypes_csv}'
    datatype_list = get_csv_as_dict(file_path=datatype_csv_file)

    # # # import SKOS mapping
    # skos_csv_file = f'{csv_prefix}/{skos_csv}'
    # skos_list = get_csv_as_dict(file_path=skos_csv_file)

    # Validate columns in CSV input
    term_valid = validate_csv(csv_import=term_list, config=config, csv_name=term_csv)
    class_valid = validate_csv(csv_import=class_list, config=config, csv_name=class_csv)
    type_valid = validate_csv(csv_import=datatype_list, config=config, csv_name=datatypes_csv)
    # skos_valid = validate_csv(csv_import=skos_list, config=config, csv_name=skos_csv)

    if False in [term_valid, class_valid, type_valid]:
        print('Check CSVs for missing required columns')

    else:

        # For each class, setup terms as json-schema
        for class_row in class_list:

            class_terms = convert_csv_to_json(
                json_prefix=json_prefix,
                rows=term_list,
                class_row=class_row,
                datatypes=datatype_list
                )

            # Write class's json-schema file
            if len(class_terms) > 0:

                # Check if dir for OUTPUT_JSON_PATH exists, and if not, make it
                if not os.path.isdir(json_output_path):
                    os.makedirs(json_output_path)

                class_filename = prep_class_name(class_row['display_label'])

                json_filename = f'{json_output_path}/{class_filename}.json'
                with open(json_filename, mode='w', encoding='utf-8') as file_output:
                    json.dump(class_terms, file_output, indent=2, ensure_ascii=False)

        print(f'...JSON Schema output files are here: "{json_output_path}/"')


if __name__ == '__main__':
    main()
