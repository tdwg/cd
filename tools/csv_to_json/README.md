## csv-to-json

A script to convert the Latimer Core schema from CSV to JSON-Schema


### Setup/Requirements:

- Check your Python version by opening a command line/terminal and entering: `python3 --version` or `python --version`
- If needed, install or update Python. See specific suggestions for [Windows](https://learn.microsoft.com/en-us/windows/python/beginners#install-python), [Mac](https://www.makeuseof.com/how-to-install-python-on-mac/), or [general info](https://www.python.org/downloads/)


### How to run csv-to-json

1. Clone this repo

2. Resave the `tools/csv_to_json/.env.example` file as  `tools/csv_to_json/.env`
  - Edit any of the env variables to point to different file/paths as needed.

3. At a command line, do the following:
    `cd path/to/this-repo/tools/csv_to_json`
    `python3 csv_to_json.py`


### Troubleshooting

For problems installing required modules, try setting up virtual environment like so (if using Python 3.4+):
(after cd'ing to this repo/tools/csv-to-json)

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