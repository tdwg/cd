# Latimer Core Guidance Documentation

Version | Date | Contributors | Status
-|-|-|-
0.1 | 2022-02-10 | Matt Woodburn, Jutta Buschbom, Sarah Vincent, Kate Webbink, Maarten Trekels, Janeen Jones, Sharon Grant | Draft


## Introduction to Latimer Core documentation 

NON-NORMATIVE SUMMARY: The Latimer Core (LtC) is designed to represent metadata for groups of items (i.e., collections), individual objects within which can be represented through other emerging or current  standards (e.g., Darwin Core and Dublin Core). The classes and properties (collectively terms) aim to represent information that describes these groupings in enough detail to inform deeper discovery of the resources contained within them. Many LtC terms are borrowed or derived from those standards which are used to describe individual items. As far as possible the terms included in the standard should not preclude their use across domains. 


NORMATIVE SUMMARY: The Latimer Core (LtC) schema is a standard designed to support the representation, discovery and communication of natural science collections. The classes within the standard aim to allow a high-level representation of any given collection by providing a framework within which the set of defining characteristics shared by objects in the collection can be described. The creation of collection-level records is intended to promote visibility and use of items in collections. 

### LtC Glossary 
For the purposes of documenting the use of Latimer Core the following definitions will be used:

**Class** is the word that we use for the grouping of properties. It defines the thing we are talking about. For example: a Person, a group of objects, etc.

**Property** is a concept within a Class. These are what we can say about the thing described by the class. For example: givenName, genus, etc.

**Attributes** are the values that a property can take. Attributes can be prescribed/controlled for a particular property and can be thought of as lookup lists, or they may be uncontrolled and thought of as free-form strings. For example ‘George’, ‘Rattus’, ‘under the tree by the rock’.

**Vocabulary** is a general word for a set of classes, properties and/or attributes. 

**Controlled Vocabulary** is a prescribed set of attributes that a property can have. Controlled vocabularies improve retrieval and reuse, as well as form the basis for machine-readability and -actionability.

**Term** is a general word for either a class, a property, or an attribute, specifically for predefined attributes in the lists of controlled vocabularies.

**Range** may differ from the Resource Description Framework’s (RDF) definition of ‘range’, which applies to RDF properties and their usage within RDF triples (https://www.w3.org/TR/rdf-schema/#ch_properties).  In Latimer Core, range is meant to guide usage of properties from one LtC class in combination with properties of another LtC class.

**Repeatability**: certain classes and/or properties can be repeated. For example, a Person can have several Identifiers of different identifierTypes. A collection (i.e. an ObjectGroup) can have several instances of the CollectionStatusHistory class to describe its different states through time.

**Reusability**: several classes can be reused, that is, they can be simultaneously attached to different classes to expand the sets of properties of those classes. For example, the Identifier or TemporalCoverage classes can be used in conjunction with many other classes to describe in more detail and with enhanced functionality the identity and temporal scope of different aspects (represented by classes) of a single collection.

**Schema** is the word we use for the defined structure of the record. The schema should describe shape, structure and rules of composition. Here, we pluralize ‘schema’ as ‘schemes’ or ‘schemas’.

## Latimer Core standard and model concepts
### Audiences
There are three main audiences for this documentation:

1. Data-aggregators - users or groups who have a need to receive standardised collection descriptions.
2. Data-providers - users or groups who have collections information that they would like to share.
3. Data-users - users or groups who want to understand in more detail the information provided by LtC collection records and collection catalogues implementing the LtC standard. 

Taking into account the variety of use-cases (documented in a [github document](https://github.com/tdwg/cd/tree/master/reference/use_cases) and a [google sheet](https://docs.google.com/spreadsheets/d/1SsfwogZ88TgouDJ7EoDqXJFol-eVs7aYdFx504qJNzc/htmlview?pru=AAABfyxGPeI*Y85ToB8bLmUyzDSk3_wuuA#)) for the standard, it is intended that data-aggregators should define a minimal set of classes, properties and relationships between them that best suit their needs. CollectionDescriptionScheme classes are important in this context as a method for communicating to Data-providers the shape and types of information that they need to provide. 

## Collection Description Schemes
When describing large collections it is anticipated that the same collections can be described using different schemas for different purposes. For instance a museum collection may be described based on “famous named” collections or collectors (e.g., Darwin, Spruce) if an aggregator has the need to “find” lost specimens from previously formed collections. The same collection may be described in whole or part based on taxonomic or geographic properties for the purpose of environmental or taxonomic research or funding. The `CollectionDescriptionScheme` class is intended to provide some parameters around the purpose and expectations of the descriptions and to indicate if objects within the descriptions are assigned attributes that will cause errors in metrics if not explicitly noted.

In the example below a description record for the Insects and Invertebrate Zoology collections at the Field Museum is created and its three-term [`CollectionDescriptionScheme`](https://drive.google.com/file/d/1-JAZODO9yPfRiuluWvBkKI45EKQ0xGbn/view?usp=sharing) is included. This might be a useful scheme for GRSciColl records:

[image 1 placeholder]

Another example might be describing all the “famous” collections within a larger collection.

[image 2 placeholder]

In both of the above examples the `distinctObjects` term is ‘True’, because no metric is associated with a description that could cause objects to be counted twice. However, if the 2 examples (GRSciColl and Famous collections) are combined

[image 3 placeholder]

The `distinctObjects` term becomes ‘False’ because the count metric for the `OrganisationalUnit` contains within it the objects and metrics associated with the `ObjectGroup` (i.e. specimen count).

Latimer Core is intended to be flexible for use to accommodate as much as possible future use cases, `CollectionDescriptionScheme` serves as the “definition” of any scheme that is developed.


