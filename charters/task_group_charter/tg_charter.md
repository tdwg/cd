# Collection Descriptions Data Standard Task Group Charter

## Conveners

*   Deborah Paul ([dpaul@fsu.edu](mailto:dpaul@fsu.edu))
*   Matt Woodburn ([m.woodburn@nhm.ac.uk](mailto:m.woodburn@nhm.ac.uk))

## Core Members

*   Wouter Addink
*   Mike Trizna
*   Janeen Jones
*   Sharon Grant
*   Kate Webbink
*   Connie Rinaldo
*   Carolyn Sheffield
*   Dag Endresen
*   Holly Little
*   Ramona Walls
*   Kerstin Lehnert
*   Niels Raes
*   Dave Smith
*   Mareike Petersen
*   William Ulate
*   Donald Hobern
*   Ana Casino

## Motivation

We urgently need a core vocabulary that describes the collections themselves, not the published datasets. We need to be able to use the published dataset metrics together with collections-level metadata and metrics in order to make meaningful comparisons across collections (e.g. what's unique about a particular collection, or where are the gaps). These data are especially critical for discovering collections that are not yet publishing their specimen data anywhere. There are valuable collections that have no information stored in a database and many do not have a presence on the Internet. Some **current stakeholders** asking for such a standard include GBIF, DiSSCo, SYNTHESYS+, ICEDIG, MOBILISE, CETAF, and iDigBio and collections around the world (MfN, MOBOT, RBGE, CMN, Naturalis, The Field Museum, The Smithsonian, The NHM, and others, to name a few). Members in the group bring in relevant perspectives from other standards organizations such as the [Research Data Alliance (RDA)](https://rd-alliance.org/) as well. Other potential stakeholders include funding agencies (like conservation companies, and foundations) who are looking for certain data that are needed for addressing their missions. This metadata has the potential to expose what's available and help with prioritizing funding.

Institutional and Collection-level data currently shared along with specimen-record-level data records is often sparse and not in any way complete. This collection-level data is currently mapped to the Ecological Metadata Language (EML) standard originally developed to meet the data-sharing needs of the ecological community. Data provided in the EML data file often conflates data about what is in the dataset being shared with data about the entire collection or institution. Collections-level data are often also shared in free-text fields making automated tracking of worldwide collections status and metrics, very difficult or impossible. Development, adoption, and implementation of a carefully curated set of collections concepts will support much-needed access to collections-level information necessary for policy, regional, organization, governmental, and individual decision making. This information must be accessible via a collaboratively developed API.

## Goals, outputs and outcomes

This task group will:
*   Produce a new Collections Descriptions vocabulary for describing groups of natural collection objects. While the scope will be limited in the first instance to collections of physical and natural objects, the data standard and underlying model will be designed to be extensible to other types of collection in the future. (See full scope of CD in the [Interest Group's Charter](https://www.tdwg.org/community/cd/), under "What are collection descriptions?")
*   Create an initial resource of reference examples to support adoption of the extension
*   Target dates:
    *   Assemble use cases and complete landscape and requirements analysis, 03/2019
    *   Completion of data model design, 07/2019
    *   Completion of initial draft standards, 03/2020
    *   Review within the task group, 04/2020
    *   Completion of revised draft for submission to executive and appointment of review manager, 05/2020
    *   Initiate expert review, 05/2020
    *   Reviews submitted to executive, 07/2020
    *   Initiate public review of proposed standard, 08/2020
    *   Complete public review, 10/2020
    *   Modify draft in light of review, submit revised draft to Executive, 11/2020
    *   Standard ratified by Executive, 12/2020

## Strategy

The work will be divided across tasks found in the [task list](https://docs.google.com/spreadsheets/d/1LmQvzOUeO4gbZAnHQPYsqxOwJYg9SqdiNT4guJkJ8RU/edit?usp=sharing), with (co-)leaders assigned to each task. GitHub functionality (e.g. [issues](https://help.github.com/articles/about-issues/), [project boards](https://help.github.com/articles/about-project-boards/) and [milestones](https://help.github.com/articles/about-milestones/)) will be used to track work and progress and to communicate across groups, while a GitHub repository and Github Pages will be used to manage group content. 

Task participants will meet remotely as required, with a more formal online whole-group meeting every 3 months. The group will also plan to have physical meetings once per year and finish in two years. These events could potentially use resources from iDigBio and TDWG, and several stakeholder projects and organisations (MOBILISE, SYNTHESYS+, ICEDIG, DiSSCo, GBIF, iDigBio) are also keen to support (and possibly fund) joint meetings to speed up progress on this standard development to finish in less than two years.

The group's work will involve the following steps:

*   Review the existing draft NCD standard ([https://www.tdwg.org/standards/ncd/](https://www.tdwg.org/standards/ncd/)), and develop crosswalks of existing CD standards and methodologies.
*   Gather collections description use cases and derive user stories to capture community requirements.
*   Develop a data model to define the entities, attributes and relationships needed to support the data standard and its practical application. Validate the data model by testing against the collated use cases.
*   Develop the data standards, re-using existing terms where available and defining new terms when necessary. Identify existing vocabularies for recommended use in conjunction with the standards.
*   Achieve consensus on the data model and standards from 1) the task group members, and 2) representatives of the stakeholder projects and proposed adopters.
*   Construct standards documents based on the achieved consensus for review and ratification by the TDWG Executive.
*   Document data management and citation guidelines.
*   Generate reference examples in common formats (e.g. RDF) for a cross-section of representative use cases.
*   Identify potential extensions to the standard for other collection types, and task groups to take the work forward.

## Becoming Involved

The Task Group welcomes anyone who has a practical interest in collections descriptions, and/or has experience with providing registries and metrics, creating data standards and/or other relevant experience. To join us please send an email to the conveners.

## History/Context

The first steps in standardising collection-level description began with a European Union Framework V project known as BioCASE - the Biodiversity Collections Access Service for Europe. This project ran from November 2001 until early 2005 (more on this at the [BioCASE project website](http://www.biocase.org/whats_biocase/index.shtml)).

An [RLG](https://en.wikipedia.org/wiki/Research_Libraries_Group) Programs working group of mainly North American natural history librarians and archivists known as RAVNS (Resources AVailable in Natural Sciences) has made the BioCASE metadata standard more generally applicable, rather than dealing only with specimen collections it is now a standard that covers any type of natural history collection. Discussion at the TDWG 2004 meeting in Christchurch, New Zealand, concluded that a standard for describing natural history collections would fit well with the suite of data standards being developed on behalf of the Global Biodiversity Information Facility (GBIF). The NCD Interest Group was convened and submitted a draft standard in 2008, but that standard has never been ratified.

Meetings of the Natural Collections Descriptions (NCD) Interest Group at TDWG 2016 and TDWG 2017 confirmed the continued need for a collections description standard, with the prior work done by the NCD Interest Group as the starting point.

## Summary

The Collections Descriptions (CD) Data Standard Task Group aims to provide a data standard for describing natural scientific collections that enables the ability to provide 1) automated metrics using standardised collection descriptions and/or data derived from specimen datasets (e.g. counts of specimens) and 2) a global registry of physical collections (either digitised or non-digitised).

## Resources

*   Collection Descriptions Task Group GitHub repository ([https://github.com/tdwg/cd](https://github.com/tdwg/cd))
*   Collection Descriptions Interest Group homepage ([https://www.tdwg.org/community/cd/](https://www.tdwg.org/community/cd/))
*   Previous NCD draft data standards:
    *   Homepage ([https://www.tdwg.org/standards/ncd](https://www.tdwg.org/standards/ncd))
    *   GitHub repository ([https://github.com/tdwg/ncd/tree/master/NCD-v090_TDWG](https://github.com/tdwg/ncd/tree/master/NCD-v090_TDWG))
    *   Wiki ([https://terms.tdwg.org/wiki/Natural_Collections_Description](https://terms.tdwg.org/wiki/Natural_Collections_Description))
*   EML - Ecological Metadata Language ([http://www.dcc.ac.uk/resources/metadata-standards/eml-ecological-metadata-language](http://www.dcc.ac.uk/resources/metadata-standards/eml-ecological-metadata-language))

### How to Navigate this CD Repository
We provide an [overview of this entire CD GitHub Repository](https://github.com/tdwg/cd), so that anyone can see how all the pieces fit together and (hopefully) find what they are looking for.
