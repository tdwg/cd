# CD development tools

This folder contains some ad hoc tools used to aid in the development of the standard.

## Tools list

**TDWG CD definitions report.xlsx** - A spreadsheet attached via the Github API to the draft data model definitions in this repo's issue queue. This parses the markdown table at the top of each issue and transforms the definitions into columns. To refresh the definitions from Github, use the Data -> Refresh all function in Excel.

**TDWG CD definition conversion.xlsx** - This spreadsheet uses a similar mechanism to the above, but converts the definitions into a format matching the template provided by Steve Baskauf for converting the definitions into the TDWG web view.

**TDWG CD standard browser.pbix** - A Microsoft Power BI file, which pulls the definitions from the Github issues to create a summary dashboard. This requires Power BI Desktop (free download from https://powerbi.microsoft.com/en-us/downloads/) to open.

**csv-to-json Python script** - A python script to convert a csv formatted like the [ltc standard terms csv](standard/terms) into [JSON Schema](https://json-schema.org/) files, as shown [here](../standard/json-schema).