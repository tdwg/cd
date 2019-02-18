# Collection Descriptions Interest Group

This is the repository for the Collection Descriptions Interest Group.

## About the group

The [Collection Descriptions Interest Group](https://www.tdwg.org/community/cd/) is the parent [interest group](https://www.tdwg.org/about/process/) that is chartering a task group to develop a Collection Descriptions metadata standard.

The new Collection Descriptions standard will be a successor to the unratified draft [Natural Collections Description data standard](https://github.com/tdwg/ncd/tree/master/NCD-v090_TDWG), whose development has been discontinued.

The day-to-day operations of the Interest Group is documented in this repository. You can also track and participate in the work of the group by watching this repository and monitoring the group's [issues tracker](https://github.com/tdwg/cd/issues).  

## Members

### Conveners

| Name | Affiliation | Email |
| --- | --- | --- |
| Deborah Paul | iDigBio | [dpaul@fsu.edu](mailto:dpaul@fsu.edu) |
| Matt Woodburn | Natural History Museum London | [m.woodburn@nhm.ac.uk](mailto:m.woodburn@nhm.ac.uk) |

### Core Members

| Name | Affiliation | Email |
| --- | --- | --- |
| Wouter Addink | Naturalis Biodiversity Center | [wouter.addink@naturalis.nl](mailto:wouter.addink@naturalis.nl) |
| Mike Trizna | Smithsonian Institution | [triznam@si.edu](mailto:triznam@si.edu) |
| Janeen Jones | Field Museum | [jjones@fieldmuseum.org](mailto:jjones@fieldmuseum.org) |
| Sharon Grant | Field Museum | [sgrant@fieldmuseum.org](mailto:sgrant@fieldmuseum.org) |
| Kate Webbink | Field Museum | [kwebbink@fieldmuseum.org](mailto:kwebbink@fieldmuseum.org) |
| Connie Rinaldo | Harvard University | [crinaldo@oeb.harvard.edu](mailto:crinaldo@oeb.harvard.edu) |
| Carolyn Sheffield | Smithsonian Libraries / BHL | [sheffieldc@si.edu](mailto:sheffieldC@si.edu) |
| Dag Endresen | Univerity of Oslo Natural History Museum | [dag.endresen@nhm.uio.no](mailto:dag.endresen@nhm.uio.no) |
| Holly Little | Smithsonian Institution / National Museum of Natural History | [littleh@si.edu](mailto:littleh@si.edu) |
| Ramona Walls | CyVerse | [rwalls@cyverse.org](mailto:rwalls@cyverse.org) |
| Kerstin Lehnert | Columbia University | [lehnert@ldeo.columbia.edu](mailto:lehnert@ldeo.columbia.edu) |
| Niels Raes | Naturalis Biodiversity Center | [niels.raes@naturalis.nl](mailto:niels.raes@naturalis.nl) |
| Dave Smith | Natural History Museum London | [d.a.smith@nhm.ac.uk](mailto:d.a.smith@nhm.ac.uk) |
| Mareike Petersen | Museum für Naturkunde | [mareike.petersen@mfn.berlin](mailto:mareike.petersen@mfn.berlin) |
| William Ulate | Missouri Botanical Garden | [william_ulate_r@yahoo.com](mailto:william_ulate_r@yahoo.com) |
| Donald Hobern | GBIF | [dhobern@gbif.org](mailto:dhobern@gbif.org) |

## Collection Descriptions Standard (CD) Repository Navigation ##

Contents of this README.md page assist with understanding of how to contribute and where to find materials related to the development of the collections description data standard. Note that where needed, there exists a very brief description of contents you will find at each link shared below. This group manages development using GitHub as much as possible.

### [CD Interest Group Charter](https://github.com/tdwg/cd)  
A brief description of our group

### [CD Task Group Charter]  
A detailed description of our rationale and goals, motivation, tasks, and strategy.

### [CD Task Group Charter DRAFT](https://github.com/tdwg/cd/blob/master/charters/draft/charter_collection_descriptions_tg_DRAFT.md) 
This document outlines the goals and objectives of the task group and plan for reaching these goals. 

### [CD Projects and associated tasks](https://github.com/tdwg/cd/projects)  
We started with a [spreadsheet](https://docs.google.com/spreadsheets/d/1LmQvzOUeO4gbZAnHQPYsqxOwJYg9SqdiNT4guJkJ8RU/edit?usp=sharing) acting as a template for a Gannt-style chart of all our envisioned tasks with dependencies. From this chart, we created GitHub tasks where each group can manage tracking the issues needed for that task, complete with milestones. These tasks are now each grouped into gitHub projects.

1. [Landscape and requirements analysis](https://github.com/tdwg/cd/projects/1)  
2. [Communication plan](https://github.com/tdwg/cd/projects/2)  
3. [Data model](https://github.com/tdwg/cd/projects/3)  
4. [Data standards](https://github.com/tdwg/cd/projects/4)  
5. [Documentation](https://github.com/tdwg/cd/projects/5)  
6. [Reference examples](https://github.com/tdwg/cd/projects/6)  
7. [Develop extensions](https://github.com/tdwg/cd/projects/7)
	
### CD Way of Work
As much as possible, each group is taking on a self-selected task and will manage delivery of it as they choose (meeting as needed). They may link to working documents however they choose (google docs, other, ...) but will upload summary and completed documents directly to GitHub in the appropriate folder (e.g. [meetings](https://github.com/tdwg/cd/tree/master/meetings)) for that task. The CD TG as a whole will meet 1/x month.

### CD Events
- 2016 met at TDWG 
- 2017 met at TDWG
- 2018 met at SPNHC-TDWGNZ, with some online meetings
- 2019 plans to meet in-person and at Biodiversity Next
- 2020 deliver a standard with implementations 

### Historical Materials  
This current effort evolves from work started over 10 years ago by the Natural Collections Description Standard IG/TG group (NCD). Here we attempt to link to materials resulting from their efforts. These documents provide a foundation for the CD Group.

## Repo structure

The current repository structure is described below.

```
├── README.md                   : Description of this repository
├── LICENSE                     : Repository license
│
├── charters                    : Interest Group and Task Group charters
│   └── draft                   : Draft charters and historical versions
│
├── documents                    
│   ├── draft                   : Working folder for draft documents
│   ├── final                   : Final versions of group documents
│   ├── historical              : Historical and deprecated documents, and snapshots of exernal drafts in Google Docs etc
│   └── DOCUMENT_LINKS.md       : Links to working documents in Google Docs, Office 365 etc
│
├── meetings                    : Agendas and minutes of IG and TG meetings
│
├── reference
│   ├── crosswalks              : Crosswalks of existing and previous collection descriptions standards and initiatives
│   ├── use_cases               : Documented use cases for a collection descriptions standard
│   └── REFERENCE_LINKS.md      : Links to relevant information resources (publications, sites etc)
│
├── standard
│   ├── data_model              : Data model definitions, schemata and diagrams
│   └── vocabularies            : Controlled vocabularies, ontologies etc relevant to the standard
│
└── .gitignore                  : Files and directories to be ignored by git
```

## Preferred citation
Collections Descriptions interest group. 2019. Collection Descriptions (CD), in development. Biodiversity Information Standards (TDWG) http://www.tdwg.org/standards/