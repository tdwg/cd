---
permalink: /charter/
---

# Collection Descriptions (CD) Interest Group Charter

TDWG Interest Group

## Conveners

Deborah Paul (dpaul@fsu.edu)

Matt Woodburn (m.woodburn@nhm.ac.uk)

(Past Co-convenor, Alex Thompson)

## Current people expressing interest to work on CD

See [Member List](https://github.com/tdwg/cd/blob/master/README.md#members)

## Motivation

Evolving from the work of the Natural Collection Descriptions (NCD) group, the Collection Descriptions (CD) Interest Group is developing a Collections Description (NCD) data standard for describing entire collections of natural history materials. Examples include collections of specimens, observation data, visual resources, photographs, and materials from the many voyages of discovery that have been conducted. Collection description records contain information about the collection, access and usage of the collection and where to get more detailed information.

There are valuable collections that have no information stored in any database and many do not have a presence on the Internet. Institutional and Collection-level data currently shared along with specimen-record-level data records is often sparse and not in any way complete. This collection-level data is currently mapped to the Ecological Metadata Language (EML) standard originally developed to meet the data-sharing needs of the ecological community. Data provided in the EML data file often conflates data about what is in the dataset being shared with data about the entire collection or institution.

Collection-level information mapped to EML and currently provided with biodiversity datasets is not sufficient to answer current-day data needs for institutional, regional, national, or international planning. More and richer data about collection holdings and the institutions that house them is desperately needed for strategic prioritization of collections data mobilization. Data-sharing at this level is also problematic as it is not currently available through an API. In other words, there is no machine-to-machine data-sharing or data-update capability. This means all collections-level information worldwide must be updated by hand, by humans and is therefore quickly out-of-date and out-of-sync across disparate resources. Also, collection data provided in the EML data model cannot be used to automatically discover such information as what portion of a collection is digitized or georeferenced. The original NCD charter and work recognized many of these issues but all members of the group agree the charter needs to be updated in light of new momentum to address these needs, including plans by GBIF for the development of a new resource to manage and share collections-level data.

## Becoming Involved

The Convener would be pleased to hear from anyone, and particularly:

* those that have skills in the implementation of Web-based information systems, or
* in writing descriptions based on interviews with collection owners, or
are owners of collections that would themselves like to test and make use of the standard and associated software, or
* just have an interest in the use of collection descriptions in resource discovery systems.

## History and Context

### What is NCD?

Natural Collections Description (NCD) is a data standard for describing groups of natural history objects; one NCD record describes one entire group. This standard was implemented by the [Smithsonian Field Book Project](https://siarchives.si.edu/about/field-book-project). 

### What is CD?

As part of addressing the critical need for much better knowledge about worldwide collection holders and their holdings, this CD group recognizes the need to further develop and expand data standards to capture concepts not currently part of the EML standard. Steps are being taken at GBIF to create an automated collection-level data-sharing resource that will encompass the data currently housed in GRBio. In this sense, the CD group recognizes our path is one of *co-developing a standard and a reference implementation* and producing standards documentation on the data and data model found in this reference implementation so that others can build compatible systems. At the same time we will strive to provide a rich, but carefully curated, set of terms and relationships directed at addressing known knowledge gaps and accessibility issues. We understand the need to keep the model as simple as possible, and thoughtfully choosing what collections-level data is critical to providing policy-makers and researchers alike with the best data available when planning. Making this data available, in a structured format, with a robust API available, would mean, for example, that we could more easily show how many herbarium are digitizing - and how much is done. Visualizing institution and collections-level data of this type also presents a captivating way to show the value of this metadata.

The CD standard seeks to describe the characteristics of groups of objects that are already represented individually under other current and emerging TDWG standards such as Darwin Core (specimens, observations) or Audubon Core (images, field notebooks). This limitation is imposed so that the scope of CD can be narrowly defined to the areas in which the TDWG organization has already built up the existing body of knowledge for what constitutes useful descriptive elements.

### What are collections descriptions?

In the natural history community the nature of collections can vary widely both across and within organizations. For the purposes of this standard, a collection will simply be any group of items that share some common characteristics such that they are useful to describe as a group. Such characteristics might include:

* items that were collected or made by a particular person
* items that came from the same place
* all pages of a digitized fieldbook
* a group of records in a dataset or database
* all specimens referenced within a single publication
* specimens that belong to some taxonomic group
* all specimens collected on a research voyage
* all specimens housed within a single location
* all specimens managed by an individual curator

This group will lay out a standard methodology for enumerating those common characteristics at the group level for the purpose of communicating the existence and nature of to others. These group level characteristics may come from a variety of sources including aggregations of individual records where those records are already digitized or hand generation via manual inventories of physical collections.

### What are the uses of collection descriptions?

Some of the main areas are served by collection-level description records:

* Providing a descriptive overview of each collection
* Establishment of relationships between collections in several locations
* Resource and expertise discovery
* As an aid for collections management processes
* Provide complete metadata for other data records (e.g. specimen records)  

1. SPEED

  Collections of natural history material can be large. Consequently detailed item-level descriptions often take a long time to generate. A collection-level record can ensure that knowledge about a collection can be rapidly revealed. It is also useful to hold the details that are common to the whole collection once, rather than being repeated with the record for each item.

2. RE-UNITING SCATTERED COLLECTIONS

  "Virtual collections" are another way to link resources. Some organisations divide collections between departments for curatorial purposes. Researchers would need to contact each department individually to assess the complete collection. Similarly, some collections, such as those of Darwin, have been dispersed throughout several organisations. These collections may be re-united in a virtual sense, using collection descriptions for each component.

3. POINTER TO ITEM-LEVEL DETAIL

  Collection descriptions are verbose, and therefore complement the rows of raw data that are produced by item-level databases. A collection description record can be created for a collection whether the items in that collection have their own records in a database, or not. Where a database containing item-level details exists, a link can be provided to that database to provide more detail. If the collection does not have an item-level database, producing a collection description reduces the chances of that collection being overlooked by researchers using the Web for resource discovery.

4. TOOL TO HELP WITH COLLECTIONS DISCOVERY, MANAGEMENT, and ATTRIBUTION

  Collection descriptions enable a broad perspective. A set of collection descriptions could serve a variety of additional purposes for any organisation:

  * A collections inventory is helpful in protecting against both loss of data and loss of collections and thus serves as a form of audit control and security against unauthorised disposal.
  * It can help with the assessment of the strengths and gaps in the organisation as a whole, so that finding collaboration partners that have either the same or complementary strengths is simplified.
  * It can help to identify which areas should be a priority for development in strategic plans and to establish priorities for item-level cataloguing.
  * By recording conservation concerns, the priorities for conservation / preservation treatment can be established. Collections cannot be protected if it is not known that they exist.

5. EARLY WARNING OF TECHNOLOGICAL OBSOLESCENCE

  Collection descriptions can serve to prevent loss of data that is in a physical form or data in a format that is nearing technological obsolescence. Creating collection descriptions for datasets that includes format information will help to act as an early warning so that data can be transferred to a current format. Data then becomes part of a digital preservation programme, rather than a digital archaeology project.

6. MULTIPLE USE OF DATA

  Re-use of data is important. Collection description records can be created with the use of existing published or unpublished resources such as printed catalogues, exhibition planning documents or archival finding aids. Conversely, data recorded in the collection description records can be used to produce exhibit labels. The data can also be provided to external initiatives, some of which wish to merge data from several sources to provide regional coverage of biodiversity collections.


### CD is evolving based on the work of the NCD

The first steps in standardising collection-level description began with a European Union Framework V project known as BioCASE - the Biodiversity Collections Access Service for Europe. This project ran from November 2001 until early 2005 (more on this at the BioCASE project website.)

An RLG Programs working group of mainly North American natural history librarians and archivists known as RAVNS (Resources AVailable in Natural Sciences) has made the BioCASE metadata standard more generally applicable, rather than dealing only with specimen collections it is now a standard that covers any type of natural history collection (specimens, original artwork, photographs, archives, published material or a mixture). Discussion at the TDWG 2004 meeting in Christchurch, New Zealand, concluded that a standard for describing natural history collections would fit well with the suite of data standards being developed on behalf of the Global Biodiversity Information Facility (GBIF). The NCD Interest Group was convened and submitted a draft standard in 2008, but that standard has never been ratified. Meetings of the Natural Collections Descriptions (NCD) Interest Group at TDWG 2016 and TDWG 2017 confirmed the continued need for a collections description standard, with the prior work done by the NCD Interest Group as the starting point.

## Summary

CD plans to support first, the development of a standard for sharing metadata about collection objects in scientific collections while planning to develop the standard so that it can be expanded to other types of collections (e.g. sea water collections).

The Interest Group is developing CD for use with RDF to ensure that it integrates with TDWG's common development architecture. The standard enables the aggregation of collections descriptions from many sources and facilitates resource discovery - particularly for collections that do not have a Web presence.

## Historically

NCD is a standard between the general resource discovery standards such as Dublin Core, and the rich collections description standards such as EAD. Mappings enable the extraction of a Dublin Core record from an NCD record or, conversely, filling out an NCD record into an EAD record. The NCD Interest Group brought together work on collection descriptions being carried out for the European Union Framework VI programme known as SYNTHESYS and the work performed by RAVNS under the auspices of RLG with that carried out by TDWG members.

CD will build on NCDs effort to connect to and use and link to other standards as appropriate. 

## Resources

* To join the TDWG mailing list see: http://lists.tdwg.org/mailman/listinfo/tdwg
* CD Discussion and documents are on GitHub: https://github.com/tdwg/cd
  * The NCD Archived repo is at: https://github.com/tdwg/cd/blob/master/README.md#old-ncd-repository
  * NCD data can be found here https://github.com/tdwg/wiki-archive/tree/master/twiki/data/NCD


## Original Charter Core Members of NCD

Wouter Addink	(wouter(at)eti.uva.nl)	Technical - NCD Toolkit  
Carol Butler	(butlercr(at)si.edu)	Terminology  
Markus Döring	(m.doering(at)BGBM.org)	Technical - RDF  
Doug Holland	(doug.holland(at)mobot.org)	Data mapping  
Barbara Mathé	(mathe(at)amnh.org)	Data mapping  
Connie Rinaldo	(crinaldo(at)oeb.harvard.edu)	Documentation  
Larry Speers	(lspeers(at)gbif.org)	GBIF liaison  
Günter Waibel	(Guenter_Waibel(at)notes.rlg.org)	Resource organiser  