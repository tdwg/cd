# Use Cases 

## Index Herbariorum 

The IH search page is consistently the most-visited webpage in the NYBG Virtual Herbarium (72,998 visits in the past 12 months, or 199/day). Study of web use statistics and direct feedback from users reveals a wide user base, the main groups of which are summarized below. 

### Herbarium commerce 

Annually, herbaria send and receive an estimated 10 million specimens as loans, gifts, exchange, and other transfers. The information contained in IH allows herbaria not only to address their shipping boxes correctly, but also to assess the reliability of herbaria to which they are considering lending specimens. Herbaria use the information included in IH about staff expertise to find individuals who can provide identification or evaluation of specimens of a particular group or region. Herbaria use IH to find partners for the exchange of specimens that augment their own holdings.  

### Biodiversity surveys or evolutionary reconstructions of a taxonomic group 

Researchers use IH to find previously collected specimens that are pertinent to their studies, to determine what taxa and geographic areas are well represented and which are not (and therefore require additional study) and to develop collaborations to facilitate new field studies. In order to obtain permits for field surveys in a foreign country, it is usually essential to develop a partnership with an herbarium in that country, where one set of voucher specimens must be deposited.  Scientists conducting research in foreign countries use IH to determine the best partner in the relevant country and to make contact with those individuals.  

### Scientific journals 

Journals use IH codes in the citation of specimens examined for a given study, including the designation of type specimens in the description of new species.  Journals such as Systematic Botany, Mycologia, Brittonia and The Bryologist will not accept for publication an article describing a new species that does not cite a standard IH acronym as the place of deposition for the type specimen of a new species.

### Collaborative projects 

Collaborative projects often use IH as a tool for identifying the range of participants and resources for such projects.  For example, IH played a key role in identifying potential participants in the Global Plants Initiative (5) a project to digitize all type specimens in the world’s herbaria and serve these through a common web portal. The National Ecological Observation Network (6) has used IH to find taxonomic expertise and collection repositories near NEON sites to help with the biodiversity inventories of these sites.  The International Association of Plant Taxonomists uses IH data to determine the number of institutional votes each herbarium should have for the nomenclature session at the International Botanical Congress meetings every six years.

### U.S. Government agencies use IH for several purposes 

Collecting permits for National Parks and other protected federal lands require that specimens collected on these sites be deposited in IH listed herbaria.  The U.S.  Fish & Wildlife Service uses IH as a resource for determining whether or not an institution should be granted a permit to house endangered species (a CITES permit) and uses IH code as part of the CITES permit identifier.  Recently U.S. Fish and Wildlife used the email contact list for IH to send a questionnaire to all herbaria asking them to evaluate their experiences applying for and managing CITES permits.  Additionally, IH is used by Homeland Security to find specialists for the identification of unknown specimens confiscated at U.S. customs.  Natural Resource Managers use IH to find experts to identify species on federal lands.  The National Park Service uses IH to keep track of specimens collected in National Parks for their annual inventories and collection assessments.



## Smithsonian Field Book Project

The Field Book Project is a collaborative grant-funded initiative based at Smithsonian to catalog, digitize, and provide open access to scientists’ field notes held in the collections of the Smithsonian Institution Archives and other Smithsonian departments.

The Field Book Project cataloging approach involved creating collection level records, item level records, and authority records for people, organizations, and expeditions.  Collection level records were created using a subset of elements from NCD v.0.7.  Item level records were created using MODS (Metadata Object Description Schema, a somewhat simplified version of the widely adopted library schema MARC), and EAC-CPF (Encoded Archival Context for Corporate Bodies, Persons, and Families) for the authority files.

This use case will focus on the collection level records which were created using the subset of NCD v 0.7 data elements.  As of 23 February 2018, 658 collection records have been created by the Field Book Project. The majority of these records have been published to the Smithsonian Collections Search Center and can be viewed here: http://collections.si.edu/search/results.htm?view=&dsort=&date.slider=&q=unit_code%3AFBR+collection+name

### Collections as defined for field book description

From Nakasone, S. and Sheffield, C. Descriptive Metadata for Field Books D-Lib Magazine, Volume 19, Number 11/2 (November/December 2013) http://www.dlib.org/dlib/november13/nakasone/11nakasone.html#4 :
“A "collection" is defined as any group of field books with a unifying relationship(4). Field book collections can be assembled in many ways; Smithsonian collections, however, are usually grouped by collector or expedition. For example, a collection grouped by the collector Alexander Wetmore would consist of field books created or owned by Wetmore. Alternatively, a collection grouped by the expedition United States Exploring Expedition might consist of field books created by various individuals that participated in that expedition. Less frequently, collections are assembled by the organizations as a creator. However they are grouped, collections are determined based on the way the field books were physically organized, with respect to the provenance and order in which they were received and maintained, prior to our involvement, in accordance with archival practice.”(5)  

4. Society of American Archivists, Describing archives: A content standard, (Chicago: Society of American Archivists, 2004),, 203.  

5. We retain the organization of collections already accessioned by SIA. We use descriptive information in finding aids, when available, as a spring board for our own records and to maintain consistency. For collections maintained by museum departments, generally each collector is given her own collection because that is how the museum organizes it. If the museum chose another way to organize a collection, for example, kept all the field books inherited by another museum together as one group, we would organize the collection in the same way.  

### NCD 0.7 as used by Smithsonian Field Book Project 

These collection records are currently used to aggregate item records from a single field book collection together on the Smithsonian Collections Search Center (SI-CSC): http://collections.si.edu/search/results.htm?view=&dsort=&date.slider=&q=unit_code%3AFBR+collection+name

Each of these collection and item records also link to the Field Book Project-produced authority profiles for persons, organizations, and/or expeditions involved in their creation. 

For more information on how the Field Book Project used NCD v0.7, the Field Book Project Cataloging Manual is available here:
https://drive.google.com/file/d/0BzbZIJVfq9rPUHQ3NDl6Y2Zha0U/view
Section 1 focuses on Collection Level Description and includes a summary of elements used followed by detailed information specific to how the Field Book Project uses those elements, including definitions, recommended data values, and examples.

## GBIF Data Management

GBIF has a multi-faceted interest in collection descriptions metadata.

### Publishing and sharing collection description metadata

Some GBIF nodes (notably Atlas of Living Australia) collect and manage collection metadata as a national-scale catalogue.  This is frequently a scale at which such information can efficiently be gathered and curated, and GBIF is interested in promoting and reinforcing this approach across its nodes, while at the same time avoiding unproductive overlaps with Index Herbariorum and other community initiatives.

### Increasing linked-open-data aspects of GBIF aggregated data

A primary goal for GBIF in aggregating and indexing specimen data (and other occurrence records) is to increase normalisation and to deduplicate diffuse text references to known concepts and entities, including e.g. countries, taxon concepts, field collection protocols, etc.  A key class of entities for which this should be possible is the set of natural history collections.  A well-managed catalogue/vocabulary of the world's NHCs would offer many opportunities to normalise collection codes/identifiers in specimen records and establish linked-open-data pathways within accessible biodiversity data.

### Collection description metadata as anchor for subsequent digitisation

Publishing a collection description can be seen as the first step in bringing a collection online and is consequently a useful point to start engagement with collections.  The description record can then serve as the anchor point for linking further digitisation products, including refining taxonomic scope through checklists, publishing Darwin Core records, and augmenting with rich digital media and other artifacts.

### Promoting data mobilisation by GBIF national nodes

A comprehensive baseline catalogue of the world's NHCs, including information on taxonomic/geographic scope and coverage and of current digitisation status, would form a key tool to support annual planning by nodes for priority actions to support or advance data mobilisation, and a baseline for measuring progress.

### Supporting researcher discovery and access for undigitised materials

GBIF is interested in understanding which collections hold currently indigitised materials, so these collecitons can be highlighted as part of some searches.  This will assist taxonomists and others in locating material and perhaps stimulating digitisation.

### Developing fundable digitisation proposals

It will be much easier to plan and seek funding for digitisation projects for a single institution or a network of related collections if there is a clear public view of what they hold and what they have to offer as part of an integrated biodiversity knowledge resource.  This is an opportunity for collections to highlight what they have that is unique.

## Field Museum of Natural History 

### Undigitized Collections Statistics
https://collections-dashboard.fieldmuseum.org
The Collections Dashboard project is an attempt to automate the process of estimating undigitized backlog (both uncatalogued and catalogued) across institutions for the purpose of revealing hidden collections and estimating digitization effort.

This use case will focus on the collection-level record structure that is required for calculating estimates of backlog, and comparing with digitized catalog record structure.  It also focuses on the need for standardized language and field structure for taxonomy and geography in collection-level records.

### Documenting Institutional Collections Through Time
The documentation of institutional collections and their changes through time has the goal of facilitating accurate attribution and collections-tracking.

This use-case will focus on the representation of an institutional collection through time, involving additions & subtractions, name-changes, and nested relationships between collection elements.

## Use Cases from [fishfindR](http://www.fishfindr.net)

A website to explore data from institutional fish collections integrated in iDigBio, a data aggregator. Using iDigBio’s specimen data API, these data can be retrieved without involving collections staff, and the data can be used in near-real time to give the most accurate snapshot of current collection holdings as they are published. This prototype website provides a framework in which all digitized collections can be analyzed and compared using data from iDigBio’s API’s. 

### Motivating collections to publish well curated data

Some institutional collections are not publishing their data for integration by a data aggregator, despite the approachability and ease of publishing data. For the most part, collections that are not published are small regional collections not associated with natural history museums, although some large institutions also are not publishing digitized data. By illuminating the relationship between data publishing and data use, collections staff see how data are used more frequently from collections who publish to aggregators and it incentivizes the push to publish their data via data aggregators which in turn increases value and use as well as expands our information on biodiversity.

### Profiling collections

Each fish collection has their own method for naming and describing themselves. Traditionally, ichthyology collections use the American Society of Ichthyologists and Herpetologists Standard Symbolic Codes for Institutional Collections to identify themselves, but individual institutional decisions can disrupt adherence to community naming conventions. Instead, many collections publish data to aggregators that obfuscates their institutional or collection affiliation and fishfindR attempts to bring them to a set of standards (ASIH codes) for use in the data reports. In addition, it is a goal of this project to motivate the fish community to work towards a set of standards for describing collections data. In addition, the community may decide that some of the data synthesized from these types of analyses might be useful in describing collections. 

### Aiding collections in communicating value

fishfindR provides tools for collections staff to compare across and within collections. In doing so collections staff can find unique characteristics of their collection. These superlatives and unique attributes can be used to help secure funding or as a lobbying tool within their institution.

### Collections community empowerment

Using the fishfindR website, it is now possible to explore and to communicate about every U.S. fish collection that is digitized and aggregated within iDigBio. The data from these analyses can be used to answer many questions related to biodiversity, conservation, behavior, and life history, and can in turn be given back to collections staff to aid in soliciting support. The goal of the fishfindR project is to give data back to collections and facilitate exploration of the data. With their data visible in an easy to analyze and approachable way collections staff will know how their data looks to end users and be empowered to make the necessary changes to better facilitate the needs of their stakeholders.

## Use Cases from Global Registry of Biodiversity Repositories [GRBio.org](http://www.grbio.org)

This list from document dated 1-April-2012 and shared at the TDWG 2016 meeting of the NCD Interest Group.

1. I’m in charge of a collection (or all collections) at a biorepository and I want to **create and/or update information** on my institution and component collections. This can include:
* Institutional name and acronym
* Collection name and code
* Address and contact information
* Domain name and websites
* Webservices
* Transfer of collections to new parent institutions
* Characteristics of the institution and/or collection
2. I’m looking for basic information about:
* A particular museum/herbarium/other biorepository institution
* particular collection within an institution
based on:
* Location: country, state, city
* Institutional name
* Institutional acronym
* Domain name
and I would like to receive information:
* As a webpage I can browse
* As a webservice response

3. I’m doing a survey/study of biorepositories and I would like to get a data dump on all institutions and their collections that can be sorted by:
* Location (country, city, state)
* Institutional name
* Institutional name
* Domain name
* Type of institution (public, private non-profit, private for-profit, museum, herbarium, etc.)
* Type of collection preservation (dry/room temperature, liquid/room temperature, cryogenic)
* Size of collection
and I would like to receive information
* As a spreadsheet
* As a CSV file
* As an SQL file
* Including information that would allow me to create a map of biorepositories

4. I found a reference to a specimen of interest
* In a publication
* In GBIF (through a taxonomic search, on a distribution map)
* On GenBank or BOLD
and I would like to receive its associated primary data and metadata.  How can I access this information:
* As a webpage I can browse
* As a webservice response

5. I am writing a scientific article and I want to include references to particular specimens. How should I cite these specimens so that
* The reader can get access to the specimen record
  * As a website
  * As a webservice response
* The reader can get access to the specimen by contacting the collection manager
* The institution can find the reference to their specimen in the literature if they are collecting impact data

6. I’m submitting data records to GenBank, GBIF or another database and I want to make sure they are traceable back to their voucher specimens in biorepositories.  I want to be able to:
* Submit a single specimen identifier and have it checked against the registry
* Submit a file with multiple specimen identifiers and have them checked against the registry
* Get a report that shows which specimen identifiers do not conform with confirmed records in the registry
* Get suggestions from the registry for correcting the non-conforming records (‘Did you mean…’)

7. I’m looking for a specimen in a collection that no longer exists.  I want to find out if it has been absorbed by another biorepository in which the specimen might be located.

## Use Cases from ICEDIG
ICEDIG is one of several design studies helping to develop the DiSSCo vision. One ICEDIG group took up the task to define the requirements for a collections digitization dashboard (CDD) for DiSSCo. As part of this task, the CDD group gathered use cases in a specific format. These use cases are available  
* from the [ICEDIG Design of a Collection Dashboard](https://drive.google.com/file/d/1RLNwHuZn0xLZuLWTrJaKiQn8IjQXwbCE/view) (Deliverable D2.3), or   
* from the [documents folder](https://github.com/tdwg/cd/blob/master/documents/final/Deliverable%20D2.3%20ICEDIG%20-%20Design%20of%20a%20Collection%20Digitisation%20Dashboard%20v1.0.docx) in this repository.

## Use Cases from Ag-Canada
Ag-Canada use cases to be added here.

# Use Case Analysis
Each group member (and other interested parties) are asked to break down each use case (above) using the "epic stories format" that comes from the Agile Software Development methodology. This consists of identifying the Actor and the Actor's role, and what they would like to be able to do, if they had the necessary collections metadata available.  

* Please use [this form](https://docs.google.com/spreadsheets/d/1SsfwogZ88TgouDJ7EoDqXJFol-eVs7aYdFx504qJNzc/edit?usp=sharing "Google Sheet for Use Case Analysis") to add your analysis of the above use cases. Those developing the data model will use these data to test the model scenarios to help insure we will be able to do (share) the kinds of tasks we want to do with this information.



