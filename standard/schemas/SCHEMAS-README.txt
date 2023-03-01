Latimer Core Schemas README

//---------------------------------------------------------------------------//
The structure of the Latimer Core term csv files is defined in a set of vocabulary schema JSON files.
These vocabulary schema files share a hierarchical structure which is defined in a standards compliant JSON Schema file.

------------------------
Change History
Version 1.0 > Version 2.0
20230301
The structure of the original vocabulary schemas (which were previously labeled as json schemas) was altered to 
proper format for generating a single json schema for all vocabulary schemas. In version 1.0, each term was the 
** for the term properties, which is problematic for schemas. The term was moved to the term object using the key 
"name". Then each object defines a term in an array called properties

Version 2.0
The structure of each vocabulary schema is defined in a JSON Schema file compliant with Draft 2020-02 of the JSON 
Schema SpecificaTION (*). These term-specific json schemas were merged into a single schema that can be used for 
any vocabulary schema file. This file is referred to as the Latimer Core Schema (latimer-core-schema.json).

File Naming Specification
The filename for each vocabulary schema file adheres to a standard practice as follows
Term name in all lowercase letter with words separated by hyphens. The extension is json with no further annotations.
Example: 
Term: Address
Vocabulary Schema: address.json

------------------------
Created: 20230301
Last Updated: 20230301
Status: In Progress
ben.norton@naturalsciences.org
