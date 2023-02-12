'''Validate an LtC JSON record'''

import dotenv
import jsonschema
import requests

def main():
    '''Validate an LtC JSON record against an LtC JSON Schema'''

    # Get env variables/input
    config = dotenv.dotenv_values(".env")
    input_json_url = config['INPUT_JSON_URL']
    schema_json_url = config['SCHEMA_JSON_URL']


    # Retrieve JSON
    input_json = requests.request(
        "GET",
        input_json_url).json()

    schema_json = requests.request(
        "GET",
        schema_json_url).json()


    # Validate record-instance against schema
    print(jsonschema.validate(instance=input_json, schema=schema_json))


if __name__ == '__main__':
    main()