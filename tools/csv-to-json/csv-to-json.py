import csv
import dotenv
import genson
import json
import os
import re
import sys
# from genson import SchemaBuilder

# import CSV
def import_csv_as_dict(file: str) -> list:
    '''Returns a list of rows (dicts) from an input CSV file'''
    rows = []
    with open(file, encoding='utf-8', mode = 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for r in reader: rows.append(r)

    return rows


# setup Ltc Class List
def get_class_list(term_list: list) -> list:
    '''Get unique list of Classes defined in Latimer Core'''
    
    class_list = []

    for term in term_list:
        if 'tdwgutility_organizedInClass' in term.keys():
            class_name = term['tdwgutility_organizedInClass']
            if class_name not in class_list:
                class_list.append(class_name)
        
    return class_list


def prep_class_name(class_name):
    '''convert CamelCase class name to kebab-case'''

    class_name_prepped = re.sub(r'([A-Z])', r'-\g<1>', class_name)
    class_name_prepped = re.sub(r'^\-', '', class_name_prepped.lower())

    return class_name_prepped


# translate csv-columns to corresponding json-schema attribute
def convert_csv_to_json(rows: list, class_name: str):
    '''convert each csv-column to corresponding json-schema attribute'''

    json_schema_prepped = []

    class_name_prepped = prep_class_name(class_name)
    repo_uri_prefix = dotenv.dotenv_values('URI_PREFIX')

    # get env vars

    class_skeleton = {
        '$schema': 'https://json-schema.org/draft-04/schema',
        '$id': f'{repo_uri_prefix}{class_name_prepped}.json',
        'title': ''
    }

    for row in rows:
        if row['tdwgutility_organizedInClass'] == class_name:
            term = {}
            term['id'] = row['label']

            json_schema_prepped.append(term)

    return json_schema_prepped


def main():
    '''main script'''

    # Get input
    if len(sys.argv) > 1:
        input_csv_file = sys.argv[1]
    else:
        input_csv_file = '../../standard/terms/ltc_standard_terms*'

    # import CSV
    term_list = import_csv_as_dict(file=input_csv_file)

    # Get list of Classes
    class_list = get_class_list(term_list=term_list)

    # For each class, setup terms as json-schema
    for class_name in class_list:

        class_terms = convert_csv_to_json(rows=term_list, class_name=class_name)

        # Write class's json-schema file
        if len(class_terms) > 0:
            
            # Check if dir exists, and if not, make it
            output_path = './json_schema_output/'
            if not os.path.isdir(output_path):
                os.makedirs(output_path)

            class_filename = re.sub(r'([A-Z])', r'-\g<1>', class_name)
            class_filename = re.sub(r'^\-', '', class_filename.lower())

            json_filename = f'{class_filename}.json'
            with open(output_path + json_filename, mode='w', encoding='utf-8') as file_output:
                json.dump(class_terms, file_output, indent=True, ensure_ascii=False)


if __name__ == '__main__':
    main()
