# csv-to-json

A python script to convert CSVs formatted like the [LtC standard terms CSVs](../../standard/terms) into [JSON Schema](https://json-schema.org/) files, as shown [here](../../standard/json-schema)


## Setup/Requirements:

- Check your Python version by opening a command line/terminal and entering: `python3 --version` or `python --version`
- If needed, install or update Python. See specific suggestions for [Windows](https://learn.microsoft.com/en-us/windows/python/beginners#install-python), [Mac](https://www.makeuseof.com/how-to-install-python-on-mac/), or [general info](https://www.python.org/downloads/)


## How to run csv-to-json

1. Clone this repo

2. Resave the `tools/csv_to_json/.env.example` file as  `tools/csv_to_json/.env`
    - See [env variable descriptions](#env-variable-descriptions) below if you need help pointing to different paths or files.

3. At a command line, do the following:
    - Go to the directory containing this script

    `cd path/to/this-repo/tools/csv_to_json`

    - install required python modules listed in [`requirements.txt`](requirements.txt)

    `pip3 install -r requirements.txt`

    - run this script

    `python3 csv_to_json.py`

    - command-line output should look similar to this:

    ```
    ltc_standard_terms_draft.csv valid -- required columns all present
    ltc_categories.csv valid -- required columns all present
    ltc_datatypes.csv valid -- required columns all present
    ...JSON Schema output files are here: "test_json_schema_output/"
    ```

    Check the output-path for JSON Schema output files


### env Variable Descriptions

After you resave the [`.env.example`](.env.example) file as `.env`, open it in a text-editor and update its variable values as needed:

- `URI_RAW_PREFIX` = the GitHub (or other host) URL repo-prefix for raw CSV input files -- e.g. "https://raw.githubusercontent.com/tdwg/cd"
- `REPO_BRANCH` = the repo branch name -- e.g. "master" or "review"
- `REPO_PATH_TO_CSV` = in the repo branch, the path to the directory containing CSV files
- `REPO_PATH_TO_JSON` = not currently used, but the path to the directory containing JSON schema files

- `CLASS_CSV` = the filename for the CSV with Class definitions -- e.g. "ltc_categories.csv"
    - required column-names are: 
    - 'display_comments'
    - 'display_label'

- `TERM_CSV` = filename for the term definitions CSV -- e.g. "ltc_standard_terms_draft.csv"
    - required column-names are: 
    - 'definition'
    - 'label'
    - 'rdf_type'
    - 'tdwgutility_required'
    - 'tdwgutility_organizedInClass'
    - 'term_localName'

- `DATATYPES_CSV` = filename for datatype-definitions CSV -- e.g. "ltc_datatypes.csv" (can be same CSV )
    - required column-names are:
    - 'datatype'
    - 'tdwgutility_organizedInClass'
    - 'term_localName'

- `SKOS_CSV` = "ltc_skos_mapping.csv"

- `SPEC_CSV` = the full URL to a CSV containing term requirements/restrictions for a particular implementation of Latimer Core.
    - CSV columns are based on those of the `TERM_CSV`
    - e.g.: https://raw.githubusercontent.com/tdwg/cd/auto-json-spec/tools/csv_to_json/test_spec_input/test_spec_terms_draft.csv


- `JSON_OUTPUT_PATH` = the path where output JSON Schema files from `csv_to_json.py` will go, relative to "tools/csv_to_json/" -- e.g.:
    - to output to a test subdirectory, use "test_subdirectory"
    - to output to (and overwrite) the live directory for Latimer Core, use "../../standard/json_schema_output"

- `SPEC_JSON_OUTPUT_PATH` = the path where output JSON Schema files from `csv_to_json_spec.py` will go, relative to "tools/csv_to_json/" -- e.g.:



### Troubleshooting

####  ModuleNotFoundError
When you try "How to" step 3, if you get an error like this:
    ```
    Traceback (most recent call last):
    File "/Users/oldadministrator/Documents/cd/tools/csv_to_json/csv_to_json.py", line 8, in <module>
        import requests
    ModuleNotFoundError: No module named 'requests'
    ```

Install the missing module -- "requests" in this example, like so:

`pip3 install requests` or `pip install requests`

Reminder:  if you get multiple errors like that, re-try installing modules listed in [requirements.txt](requirements.txt):

`pip3 install -r requirements.txt`


#### Virtual environment
If you still have errors running or installing modules, try setting up a [python virtual environment](https://docs.python.org/3/library/venv.html) like so:

1. Make sure you're using Python 3.4+
    `python3 --version`  or  `python --version`

2. `cd` to this repo/tools/csv_to_json

3. Activate a virtual environment like so:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

    #### Possible note for PC setup:
    If step 2 didn't work, try: 

    ```
    # In cmd.exe
    venv\Scripts\activate.bat
    # In PowerShell
    venv\Scripts\Activate.ps1
    ```

4. After activating the virtual env, retry installing requirements and running the script:

    - install required python modules

    `pip3 install -r requirements.txt`  or  `pip install -r requirements.txt`

    - run this script

    `python3 csv_to_json.py`  or  `python csv_to_json.py`


## To Do

### 1. Datatype - date & date-time

Handle dates as string-datatypes with special formatting, e.g. ltc:startedAtTime in ltc:PersonRole:

```
    "startedAtTime": {
        "description": "The date or time when a Person started fulfilling the role specified in the role property.",
        "type": "string",
        "oneOf": [
            {
                "format": "date"
            },
            {
                "format": "date-time"
            }
        ]
    }
```

### 2. Validator
- Add validator to check LtC records against LtC JSON Schema