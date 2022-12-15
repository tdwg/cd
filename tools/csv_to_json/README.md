## csv-to-json

A script to convert the Latimer Core schema from CSV to JSON-Schema


### Setup/Requirements:

- Check your Python version by opening a command line/terminal and entering: `python3 --version` or `python --version`
- If needed, install or update Python. See specific suggestions for [Windows](https://learn.microsoft.com/en-us/windows/python/beginners#install-python), [Mac](https://www.makeuseof.com/how-to-install-python-on-mac/), or [general info](https://www.python.org/downloads/)


### How to run csv-to-json

1. Clone this repo

2. Resave the `tools/csv_to_json/.env.example` file as  `tools/csv_to_json/.env`

  - Edit any of the `env` variables to point to different file/paths as needed:

    - `URI_RAW_PREFIX` = the GitHub (or other host) URL repo-prefix for raw CSV input files -- e.g. "https://raw.githubusercontent.com/tdwg/cd"
    - `REPO_BRANCH` = the repo branch name -- e.g. "master" or "review"
    - `REPO_PATH_TO_CSV` = in the repo branch, the path to the directory containing CSV files
    - `REPO_PATH_TO_JSON` = not currently used, but the path to the directory containing JSON schema files

    - `LTC_CLASS_CSV` = the filename for the CSV with Class definitions -- e.g. "ltc_categories.csv"
      - required column-names are: 
        - 'display_comments'
        - 'display_label'

    - `LTC_TERM_CSV` = filename for the term definitions CSV -- e.g. "ltc_standard_terms_draft.csv"
      - required column-names are: 
        - 'definition'
        - 'label'
        - 'rdf_type'
        - 'tdwgutility_required'
        - 'tdwgutility_organizedInClass'
        - 'term_localName'

    - `LTC_DATATYPES_CSV` = filename for datatype-definitions CSV -- e.g. "ltc_datatypes.csv" (can be same CSV )
      - required column-names are:
        - 'datatype'
        - 'tdwgutility_organizedInClass'
        - 'term_localName'
        
    - `LTC_SKOS_CSV` = "ltc_skos_mapping.csv"

    - `JSON_OUTPUT_PATH` = the path where output JSON Schema files will go, relative to "tools/csv_to_json/" -- e.g.:
      - to output to a test subdirectory, use "test_subdirectory"
      - to output to (and overwrite) the live directory for Latimer Core, use "../../standard/json_schema_output"


3. At a command line, do the following:

    - Go to the directory containing this script

    `cd path/to/this-repo/tools/csv_to_json`

    - install required python modules

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


### Troubleshooting

For problems installing required modules, try setting up virtual environment like so (if using Python 3.4+):

1. `cd` to this repo/tools/csv_to_json

#### PC:
```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

#### Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

2. In the virtual env, retry installing requirements and running the script

    - install required python modules

    `pip3 install -r requirements.txt`

    - run this script

    `python3 csv_to_json.py`