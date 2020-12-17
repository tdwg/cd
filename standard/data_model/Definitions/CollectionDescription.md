# ObjectGroup 

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Core class |
| **Hierarchy** | no |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** | NA |
| **Notes** | We may need a better term for the core class, as it represents a grouping of collection objects rather than a description per se. Makes it difficult to refer to coherently in property definitions and discussions. CollectionGroup, CollectionCluster...? |


## Header (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | NA |
| **Definition** | Information about the ObjectGroup digital record |
| **Repeatable** |  |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** | Class name & concept borrowed from NCD standard |

### recordID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A unique identifier to the collection description record |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** | yes |
| **Repeatable** | no |
| **Constraints** | unique |
| **Examples** |  |
| **Notes** |  |

### accessRights (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Information about who can access the resource or an indication of its security status. |
| **Dimension** |  |
| **Existing property** | dc:accessRights |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/accessRights |
| **Format** | Text |
| **Required** | no |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | These data are considered to be in the public domain |
| **Notes** |  |

### license (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A legal document giving official permission to do something with the resource. |
| **Dimension** |  |
| **Existing property** | dc:license |
| **Existing class** | Rights |
| **Existing property identifier** | http://purl.org/dc/terms/license |
| **Format** | URI |
| **Required** | yes |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | https://creativecommons.org/licenses/by/4.0/deed.en
https://creativecommons.org/publicdomain/zero/1.0/
https://creativecommons.org/licenses/by/4.0/legalcode |
| **Notes** | Recommended practice is to identify the license document with a URI. If this is not possible or feasible, a literal value that identifies the license may be provided. |

### recordRights (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Information about rights held in and over the resource. |
| **Dimension** |  |
| **Existing property** | dc:rights |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/rights |
| **Format** | URI |
| **Required** | yes |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | Typically, rights information includes a statement about various property rights associated with the resource, including intellectual property rights. Recommended practice is to refer to a rights statement with a URI. If this is not possible or feasible, a literal value (name, label, or short text) may be provided. |

### rightsHolder (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A person or organization owning or managing rights over the resource. |
| **Dimension** |  |
| **Existing property** | dc:rightsHolder |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/rightsHolder |
| **Format** | URI |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | ecommended practice is to refer to the rights holder with a URI. If this is not possible or feasible, a literal value that identifies the rights holder may be provided. |

### creator (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | An entity responsible for making the resource. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** | dc:creator |
| **Existing property identifier** | http://purl.org/dc/terms/creator |
| **Format** | URI |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | Recommended practice is to identify the creator with a URI. If this is not possible or feasible, a literal value that identifies the creator may be provided. Equivalent property: http://xmlns.com/foaf/0.1/maker |

### recordSource (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Source of the record if not created by the author named in `creator` |
| **Dimension** |  |
| **Existing property** | dc:source |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/source |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### recordCreatedDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Date of creation of the resource. |
| **Dimension** |  |
| **Existing property** | dc:created |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/created |
| **Format** |  |
| **Required** | yes |
| **Repeatable** |  |
| **Constraints** | ISO 8601 |
| **Examples** | 2019-12-16T09:49:51Z |
| **Notes** |  |

### editor (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | An entity responsible for making contributions to the resource. |
| **Dimension** |  |
| **Existing property** | dc:contributor |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/elements/1.1/contributor |
| **Format** |  |
| **Required** | yes |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | The guidelines for using names of persons or organizations as creators also apply to contributors. Typically, the name of a Contributor should be used to indicate the entity. In the context of CD it is the last Person that edited the record. |

### recordEditedDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Date on which the resource was changed. |
| **Dimension** |  |
| **Existing property** | dc:modified |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/modified |
| **Format** |  |
| **Required** | yes |
| **Repeatable** |  |
| **Constraints** | ISO 8601 |
| **Examples** | 2019-12-16T09:49:51Z |
| **Notes** | Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty. |

### language (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The language or communication system in which the collection desciption is written |
| **Dimension** |  |
| **Existing property** | ead:language |
| **Existing class** |  |
| **Existing property identifier** | https://www.loc.gov/ead/tglib/elements/language.html |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

## CollectionDescription (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | |
| **Definition** | A group of physical collection objects with one or more common characteristics. |
| **Repeatable** |  |
| **Relationships** | See dimensions |
| **Potential standards/vocabularies/ontologies to adopt** | Potential to align with PROV-O (e.g. https://www.w3.org/TR/prov-o/#Collection) |
| **Notes** | Properties listed as dimensions are potentially repeatable (1:n), but doing so prevents metrics from being aggregated against them. Also ref SchemeDimension subclass of CollectionDescriptionScheme.	|

### collectionDescriptionID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Unique persistent identifier for the CollectionDescription |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** |  |
| **Constraints** | GUID? |
| **Examples** |  |
| **Notes** |  |

### title (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Short title that summarises the collection objects contained within the Collection Description |
| **Dimension** |  |
| **Existing property** | dc:title |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/elements/1.1/title |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### description (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Longer description or narrative about the collection that the CollectionDescription record describes |
| **Dimension** |  |
| **Existing property** | dc:description |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/elements/1.1/description |
| **Format** | Text |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### citationText (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Recommended citation for the collection as suggested by the institution |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### onlineResources (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Online presence (which portals hold information on the collection) |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | List |
| **Required** | no |
| **Repeatable** | Yes |
| **Constraints** |  |
| **Examples** | http://www.botanicalcollections.be/#/en/home |
| **Notes** |  |

### thematicFocus (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A texual description of the collection and the characteristics and its idiosyncrasies |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### collectionStrength (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A textual description of the strengths of the collection |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** | Yes |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | Overlap with thematic focus? |

### objectType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The physical type of object that is curated as a single specimen |
| **Dimension** | Yes |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** | Controlled vocabulary |
| **Examples** | pressed dried specimen, pinned, wood block, skin, skeleton |
| **Notes** |  |

### preservationMethod (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The means by which specimens are preserved to ensure they persist for the long term |
| **Dimension** | Yes |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | List |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |

### collectionEvent (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The collection is the product of a single scientific expedition |
| **Dimension** | Yes |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | List |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |

### collectionMethod (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The method by which the specimens in the collection have been gathered  |
| **Dimension** | Yes |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | List |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |

### collectionStartDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Start date of the temporal scope within which the specimens were collected |
| **Dimension** | Yes |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Date |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** | ISO 8601 date format, resolved to day, month or year |
| **Examples** | 1886, 1984-09, 2001-10-22 |
| **Notes** |  |

### collectionEndDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | End date of the temporal scope within which the specimens were collected |
| **Dimension** | Yes |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Date |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** | ISO 8601 date format, resolved to day, month or year |
| **Examples** | 1886, 1984-09, 2001-10-22 |
| **Notes** |  |

### collectionHazard (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Potential hazardous materials used for the preservation of the specimen |
| **Dimension** | Yes? |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | yes |
| **Constraints** | controlled vocabulary |
| **Examples** | Formaldehyde, napthalene, arsenic |
| **Notes** |  |

### culturalAffiliation (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Any cultural groups affiliated (e.g., as owners or creators) with the collection |
| **Dimension** | Yes? |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |

### ecoregion (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | High level biogeographic region of the collection |
| **Dimension** | yes |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | text |
| **Required** | no |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Deserts and xeric shrublands; Tropical and subtropical moist broadleaf forests |
| **Notes** | Potential vocabulary: World Wildlife Fund ecoregions https://www.worldwildlife.org/biome-categories/terrestrial-ecoregions and https://www.worldwildlife.org/publications/marine-ecoregions-of-the-world-a-bioregionalization-of-coastal-and-shelf-areas |