# Latimer Core Guidance Documentation

Version | Date | Contributors | Status
-|-|-|-
0.1 | 2022-02-10 | Matt Woodburn, Jutta Buschbom, Sarah Vincent, Kate Webbink, Maarten Trekels, Janeen Jones, Sharon Grant | Draft

## Table of contents
1. [Introduction to Latimer Core documentation](#introduction-to-latimer-core-documentation)
2. [Latimer Core standard and model concepts](#latimer-core-standard-and-model-concepts)
    - [Audiences](#audiences)
    - [Collection Description Schemes](#collection-description-schemes)
    - [Classes and properties](#classes-and-properties)
    - [Core elements of the standard](#core-elements-of-the-standard)
      - [The ObjectGroup concept](#the-objectgroup-concept)
        - [What can an ObjectGroup represent?](#what-can-an-objectgroup-represent)
      - [Institutions and organisational units](#institutions-and-organisational-units)


## Introduction to Latimer Core documentation 

NON-NORMATIVE SUMMARY: The Latimer Core (LtC) is designed to represent metadata for groups of items (i.e., collections), individual objects within which can be represented through other emerging or current  standards (e.g., Darwin Core and Dublin Core). The classes and properties (collectively terms) aim to represent information that describes these groupings in enough detail to inform deeper discovery of the resources contained within them. Many LtC terms are borrowed or derived from those standards which are used to describe individual items. As far as possible the terms included in the standard should not preclude their use across domains. 

NORMATIVE SUMMARY: The Latimer Core (LtC) schema is a standard designed to support the representation, discovery and communication of natural science collections. The classes within the standard aim to allow a high-level representation of any given collection by providing a framework within which the set of defining characteristics shared by objects in the collection can be described. The creation of collection-level records is intended to promote visibility and use of items in collections. 


### LtC Glossary 
For the purposes of documenting the use of Latimer Core the following definitions will be used:

- **Class** is the word that we use for the grouping of properties. It defines the thing we are talking about. For example: a Person, a group of objects, etc.

- **Property** is a concept within a Class. These are what we can say about the thing described by the class. For example: givenName, genus, etc.

- **Attributes** are the values that a property can take. Attributes can be prescribed/controlled for a particular property and can be thought of as lookup lists, or they may be uncontrolled and thought of as free-form strings. For example ‘George’, ‘Rattus’, ‘under the tree by the rock’.

- **Vocabulary** is a general word for a set of classes, properties and/or attributes. 

- **Controlled Vocabulary** is a prescribed set of attributes that a property can have. Controlled vocabularies improve retrieval and reuse, as well as form the basis for machine-readability and -actionability.

- **Term** is a general word for either a class, a property, or an attribute, specifically for predefined attributes in the lists of controlled vocabularies.

- **Range** may differ from the Resource Description Framework’s (RDF) definition of ‘range’, which applies to RDF properties and their usage within RDF triples (https://www.w3.org/TR/rdf-schema/#ch_properties).  In Latimer Core, range is meant to guide usage of properties from one LtC class in combination with properties of another LtC class.

- **Repeatability**: certain classes and/or properties can be repeated. For example, a Person can have several Identifiers of different identifierTypes. A collection (i.e. an ObjectGroup) can have several instances of the CollectionStatusHistory class to describe its different states through time.

- **Reusability**: several classes can be reused, that is, they can be simultaneously attached to different classes to expand the sets of properties of those classes. For example, the Identifier or TemporalCoverage classes can be used in conjunction with many other classes to describe in more detail and with enhanced functionality the identity and temporal scope of different aspects (represented by classes) of a single collection.

- **Schema** is the word we use for the defined structure of the record. The schema should describe shape, structure and rules of composition. Here, we pluralize ‘schema’ as ‘schemes’ or ‘schemas’.


## Latimer Core standard and model concepts

### Audiences
There are three main audiences for this documentation:

1. Data-aggregators - users or groups who have a need to receive standardised collection descriptions.
2. Data-providers - users or groups who have collections information that they would like to share.
3. Data-users - users or groups who want to understand in more detail the information provided by LtC collection records and collection catalogues implementing the LtC standard. 

Taking into account the variety of use-cases (documented in a [github document](https://github.com/tdwg/cd/tree/master/reference/use_cases) and a [google sheet](https://docs.google.com/spreadsheets/d/1SsfwogZ88TgouDJ7EoDqXJFol-eVs7aYdFx504qJNzc/htmlview?pru=AAABfyxGPeI*Y85ToB8bLmUyzDSk3_wuuA#)) for the standard, it is intended that data-aggregators should define a minimal set of classes, properties and relationships between them that best suit their needs. CollectionDescriptionScheme classes are important in this context as a method for communicating to Data-providers the shape and types of information that they need to provide. 

## Collection Description Schemes
When describing large collections it is anticipated that the same collections can be described using different schemas for different purposes. For instance a museum collection may be described based on “famous named” collections or collectors (e.g., Darwin, Spruce) if an aggregator has the need to “find” lost specimens from previously formed collections. The same collection may be described in whole or part based on taxonomic or geographic properties for the purpose of environmental or taxonomic research or funding. The `CollectionDescriptionScheme` class is intended to provide some parameters around the purpose and expectations of the descriptions and to indicate if objects within the descriptions are assigned attributes that will cause errors in metrics if not explicitly noted.

In the example below an LtC description record for the Insects and Invertebrate Zoology collections at the Field Museum is created and its three-term [`CollectionDescriptionScheme`](https://drive.google.com/file/d/1-JAZODO9yPfRiuluWvBkKI45EKQ0xGbn/view?usp=sharing) is included.

  <img width="550" alt="A diagram of how Collections in the GRSciColl Collection Registry can be described with terms in the OrganisationalUnit class" src="https://user-images.githubusercontent.com/8563362/169345605-6829ee01-21ca-4f3c-8929-a6b267810443.png">

  **Figure 1:** An example record-structure that might be a useful scheme for [GRSciColl](https://www.gbif.org/grscicoll) records.


  <img width="550" alt="A diagram of how Named Collections can be described with terms in the LtC ObjectGroup class" src="https://user-images.githubusercontent.com/8563362/169345590-2517e08c-6886-4428-a6ea-ea230f7f6501.png">

  **Figure 2:** Another example record-structure of a way to describe all of the “famous” collections within a larger collection.


In both of the above examples the `distinctObjects` term is ‘True’, because no metric is associated with a description that could cause objects to be counted twice. However, if the two examples (GRSciColl and Famous collections) are nested in a single record, the `distinctObjects` term needs to be 'False'.

  <img width="550" alt="A diagram of a Latimer Core record that combines the previous examples, and has non-distinct objects" src="https://user-images.githubusercontent.com/8563362/169403099-4df8fc98-6e07-47c1-bf66-2aebcde98657.png">

  **Figure 3:** An example of a record-structure that combines ObjectGroups from the above examples, and has overlapping "Specimen Count" measurements.


The `distinctObjects` term becomes ‘False’ because the count metric for the `OrganisationalUnit` contains within it the objects and metrics associated with the `ObjectGroup` (i.e. specimen count).

Latimer Core is intended to be flexible for use to accommodate as much as possible future use cases, `CollectionDescriptionScheme` serves as the “definition” of any scheme that is developed.


### Classes and properties

Class Name | Description | Issue # | In v.1
-|-|-|-
Activity | An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities. | https://github.com/tdwg/cd/issues/310 | No
Address | A physical postal address for an organisational unit or person. | https://github.com/tdwg/cd/issues/208 | Yes
ChronometricAge | The age of a specimen or related materials that is generated from a dating assay. | https://github.com/tdwg/cd/issues/268 | Yes
CollectionDescriptionScheme | A grouping of multiple ObjectGroups for a particular use case, purpose or implementation. | https://github.com/tdwg/cd/issues/109 | Yes
CollectionStatusHistory | A historical log of changes to and statuses of the described collection over time. | https://github.com/tdwg/cd/issues/120 | Yes
ContactDetail | Details of a method by which an entity such as a Person or OrganisationalUnit may be contacted. | https://github.com/tdwg/cd/issues/329 | Yes
Event | An action that occurs at some location during some time. | https://github.com/tdwg/cd/issues/362 | Yes
GeographicOrigin | The geographic location from which objects associated with the CollectionDescription were collected. | https://github.com/tdwg/cd/issues/131 | Yes
GeologicalContext | Geological information, such as stratigraphy, that qualifies a region or place. | https://github.com/tdwg/cd/issues/178 | Yes
Identifier | A numeric or textual value, or reference such as an IRI, that can be used to uniquely identify the object to which it is attached. | https://github.com/tdwg/cd/issues/126 | Yes
MeasurementOrFact | A measurement of or fact about the ObjectGroup representing the objects in the collection description, or the relationship between the ObjectGroup and an associated class. | https://github.com/tdwg/cd/issues/289 | Yes
ObjectClassification | An informal classification of the type of objects within the ObjectGroup, using a hierarchical structure. | https://github.com/tdwg/cd/issues/214 | Yes
ObjectGroup | An intentionally grouped set of objects with one or more common characteristics. | https://github.com/tdwg/cd/issues/55 | Yes
OrganisationalUnit | A unit within an organisational hierarchy which may be at, above or below the institutional level. | https://github.com/tdwg/cd/issues/197 | Yes
Person | A person (alive or dead). | https://github.com/tdwg/cd/issues/219 | Yes
PersonActivity | A link between a Person and an Activity to enable the role that the Person played in the Activity to be specified. | https://github.com/tdwg/cd/issues/314 | No
PersonRole | A qualified association between a Person or OrganisationalUnit and an entity such as an ObjectGroup or MeasurementOrFact that enables the relationship to be contextualised with a specific role and time period. | https://github.com/tdwg/cd/issues/316 | Yes
RecordLevel | The machine-actionable information profile for the collection description digital object. | https://github.com/tdwg/cd/issues/43 | Yes
Reference | A reference to external resources and information related to the collection description. | https://github.com/tdwg/cd/issues/231 | Yes
ResourceRelationship | A relationship between an instance of a class in the collection description standard to another instance of the same class, or an instance of a different class in the standard. | https://github.com/tdwg/cd/issues/279 | Yes
SchemeMeasurementOrFact | A type of measurement or fact used by the CollectionDescriptionScheme, and the rules relating to its application. | https://github.com/tdwg/cd/issues/117 | Yes
SchemeTerm | A Latimer Core term used by the CollectionDescriptionScheme and the rules relating to its application. | https://github.com/tdwg/cd/issues/113 | Yes
StorageLocation | A physical location (such as a building, room, cabinet or drawer) within the holding institution where objects associated with the collection description are stored or exhibited. | https://github.com/tdwg/cd/issues/164 | Yes
Taxon | A group of organisms (sensu http://purl.obolibrary.org/obo/OBI_0100026) considered by taxonomists to form a homogeneous unit. | https://github.com/tdwg/cd/issues/269 | Yes
TemporalCoverage | A record of a time range represented by the collection within a particular context. | https://github.com/tdwg/cd/issues/333 | Yes

**Table 1:** A summary of the classes in the Latimer Core standard.


### Core elements of the standard
As described above, the Latimer Core standard (version 1) is made up of 23 classes, each with two or more properties. The central concept of the standard is the `ObjectGroup` class, which represents 'an intentionally grouped set of objects with one or more common characteristics'. 
Arranged around the `ObjectGroup` are a set of classes, such as `GeographicOrigin`, `Taxon` and `GeologicalContext`, which are commonly used to describe and classify the objects within the `ObjectGroup`. There are a set of classes (`OrganisationalUnit`, `CollectionStatusHistory` and `StorageLocation`) intended to reflect aspects of the custodianship, management and tracking of the collections, and a generic class (`MeasurementOrFact`) for storing metrics, narratives and other qualitative or quantitative measures within the standard. A further set of generic, reusable classes are included that enable common concepts (such as people, identifiers and references) to be attached to multiple classes within the standard. Finally, there’s a set of classes that are used to describe the structure of and metadata about the Latimer Core records and contents themselves.

These (loose and informal) categorisations are illustrated in Figure 4 below, and the concepts are described in more detail later in this section.

##### *(IMAGE PLACEHOLDER - TO-DO: replace diagram with an updated/more readable/less powerpointy version)*
![ltc_fig4_Approx_Categories](https://user-images.githubusercontent.com/8563362/169402924-2029116c-e3db-439f-99f2-8fd544aa6137.png)

**Figure 4:** Approximate categories for Latimer Core classes for describing the object group’s Characteristics (green), Collections custody (purple), Generic reusable information-types (dark blue), metrics (red), and Data structure and links (light blue).


#### The ObjectGroup concept
The ObjectGroup is the core class and concept of the Latimer Core standard. It represents any set of physical or digital objects that we want to describe together as a group, as opposed to representing and describing each individual separately. This will generally be for one or both of the following reasons:

1. There aren't yet, or may never be, individual digital records for all of the separate objects, but we still want to capture, use and share data about them at a higher level, or
2. There is information that applies to the group as a whole (e.g. a narrative or history, a registration number or a contact person), so we want to store this information at the group level rather than duplicating it across multiple object-level records.

In an ideal world where every object in global Natural Science collections has a fully populated and clean digital record, the first reason would disappear. Collection descriptions could then be assembled dynamically by aggregating data from the underlying object-level records. However, even in that far-off scenario where the majority of the data can be assembled automatically from object level records, there are still likely to be use cases for managing some information at the group level.


##### What can an ObjectGroup represent?
The Latimer Core definition of an ObjectGroup is 

*“An intentionally grouped set of objects with one or more common characteristics.”*

This is a purposefully broad definition that allows the standard to encompass a wide range of use cases for describing collections or their parts for different reasons. Although the most common and familiar use of collection descriptions has been to describe the collection of a particular institution, conceptually an ObjectGroup can represent any set and number of objects that need to be grouped for any purpose. This can scale from a few objects in a drawer to the sum total of all the collections of global natural science institutions: both of these can be represented by an ObjectGroup, as can any scale in between.

Some more practical examples of what may be represented by an ObjectGroup include:

- The collection of a single institution
- The herbarium collection of a single institution
- The invertebrates wet collection of a single institution
- A named collection provided by a specific donor, or collected by a significant collector
- The Mesozoic mammal collection of an institution
- The unincorporated objects of a particular department within an institution
- The objects in a single drawer, cabinet or room for inventory purposes
- A registration lot of objects brought into an institution together
- A database of images taken from collection specimens
- A dataset of butterfly observations taken as a monitoring time series
- An ex situ tree plantation rescuing remaining genotypes of European ash
- A virtual collection representing all penguin individuals and populations in zoos and aquaria worldwide
- Collections of sightings of animals as part of environmental impact/mitigation projects (e.g., [Toads on Roads](https://www.froglife.org/what-we-do/toads-on-roads/))

Each of these represent a number of objects that are grouped for a certain purpose, with one or more common characteristics (for example, belonging to the same institution, being from the same stratigraphic time period, or being collected by the same person). Those characteristics are described by the ObjectGroup’s properties and the other associated classes in Latimer Core, as summarised in Figure 5.

##### *(IMAGE PLACEHOLDER - TO-DO: replace with updated figure)*
![ltc_fig5_ObjectGroupAttributes](https://user-images.githubusercontent.com/8563362/169404880-9946e716-5b79-441c-9cef-23f93de53cb3.png)

**Figure 5:** A summary of the ObjectGroup's properties and other associated classes.


#### Institutions and organisational units

Collections are held by caregivers. Some collections start out as privately held assemblages, associated generally with a single person. Over the longer term, most surviving collections become preserved and managed by institutions, including for example public or private institutions, organisations, and corporations. Institutions are the administrative entities, which are stewards or owners of collections, provide administrative services, maintain and preserve collections, and often employ or dedicate responsible staff to actively manage collections. 

For the purpose of integration into a globally applicable collections registry schema, private collections can be considered to be held by a person of a corresponding role (e.g. “steward”) and part of a theoretical organisation (e.g. “independent operation”, “private residence”). For a more general discussion of organisations, persons and groups as agents see the FOAF Vocabulary Specification (http://xmlns.com/foaf/spec/).

In Latimer Core, the institution concept is incorporated into the more generic framework provided by “The Organization Ontology” W3C standard (https://www.w3.org/TR/vocab-org/). It is represented by the OrganisationalUnit class, which is more broadly defined as the corresponding term in the org-standard. In Latimer Core, its definition combines characteristics of both the org:Organisation and org:OrganisationalUnit classes, providing more flexibility. 

Instances of the ltc:OrganisationalUnit class can represent, in addition to institutions as complete entities, different subdivisions at different levels within an institution (e.g. departments, divisions, sections, faculties etc), as well as organisations at a higher level of the collection-holding institution (for example, a museum may be a subunit within the organisational structure of a university). Terms to be used in predefined vocabularies identifying the hierarchical position of an organisational unit within an organisational structure can be found in the “Academic Institution Internal Structure Ontology” (AIISO; https://vocab.org/aiiso/). 

OrganisationalUnits can be linked together using the ResourceRelationship class to form hierarchies or reflect more semantic associations. The relationshipOfResource property of the class should be used to describe the nature of the relationship. It is recommended best practice (see https://dwc.tdwg.org/list/#dwc_ResourceRelationship) to use a controlled vocabulary to describe those relationships. Examples of relationship types are “same as”, “part of”, “contains”. Development of controlled vocabularies can be started based on terms provided by existing standards, eg. org: [hasUnit](https://www.w3.org/TR/2014/REC-vocab-org-20140116/#org:hasUnit), [unitOf](https://www.w3.org/TR/2014/REC-vocab-org-20140116/#org:unitOf), [subOrganizationOf](https://www.w3.org/TR/2014/REC-vocab-org-20140116/#org:hasSubOrganization), [hasSubOrganization](https://www.w3.org/TR/2014/REC-vocab-org-20140116/#org:hasSubOrganization), and AIISO: [part_of](https://vocab.org/aiiso/#part_of), ([responsibilityOf](https://vocab.org/aiiso/#responsibilityOf), [responsibleFor](https://vocab.org/aiiso/#responsibleFor)).
