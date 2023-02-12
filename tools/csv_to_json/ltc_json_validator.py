'''Validate an LtC JSON record'''

import dotenv
import json
import jsonschema
import requests

def main():

    # Get env variables/input
    config = dotenv.dotenv_values(".env")
    input_json_url = config['INPUT_JSON_URL']
    schema_json_url = config['SCHEMA_JSON_URL']


    input_json = requests.request(
        "GET",
        input_json_url).json()
        # "https://raw.githubusercontent.com/jbstatgen/dissco_registry/main/LtCProfile_RecordLevel_20230203.json?token=GHSAT0AAAAAAB6JVHBRNELMBSZIY625POVKY65FPHQ").json()
        # https://raw.githubusercontent.com/tdwg/cd/review/examples/implementation%20examples/json/nhm_uk_json_example.json

    schema_json = requests.request(
        "GET",
        schema_json_url).json()
        # "https://raw.githubusercontent.com/jbstatgen/dissco_registry/main/LtCProfile_RecordLevel_20230203.json?token=GHSAT0AAAAAAB6JVHBRNELMBSZIY625POVKY65FPHQ").json()


    # ltc_record = json.load(input_json) # open(input_json, 'r', encoding='utf-8'))

    # ltc_schema = json.load(schema_json)  # open(schema_json, 'r', encoding='utf-8'))

    print(jsonschema.validate(instance=input_json, schema=schema_json))


if __name__ == '__main__':
    main()