# CollectionDescription 

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
| **Definition** | Information about the CollectionDescription digital record |
| **Repeatable** |  |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** | Class name & concept borrowed from NCD standard |

### recordID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
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
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### license (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** | dc:license |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/license |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### recordRights (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | IPR statement about the record |
| **Dimension** |  |
| **Existing property** | dc:rights |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/rights |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### rightsHolder (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** | dc:rightsHolder |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/rightsHolder |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### creator (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Person that created the record |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** | dc:creator |
| **Existing property identifier** | http://purl.org/dc/terms/creator |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### recordSource (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Source of the record if not created by the author named in Author |
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
| **Definition** | Date of record creation |
| **Dimension** |  |
| **Existing property** | dc:created |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/created |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### editor (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Person that last edited the record |
| **Dimension** |  |
| **Existing property** | dc:contributor |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/elements/1.1/contributor |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### recordEditedDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Date the record was last edited |
| **Dimension** |  |
| **Existing property** | dc:modified |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/modified |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

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
| **Potential standards/vocabularies/ontologies to adopt** | NA |
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
| **Required** |  |
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
| **Required** |  |
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
| **Required** |  |
| **Repeatable** | Yes |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### datasetDOIs (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | DOIs for public datasets related to the collection description |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | List |
| **Required** |  |
| **Repeatable** | Yes |
| **Constraints** | Valid resolvable DOI |
| **Examples** |  |
| **Notes** | Could expand to a class if more information than a DOI would be useful |

### thematicFocus (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A texual description of the collection and the characteristics and its idiosyncrasies |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
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
| **Required** |  |
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
| **Examples** |  |
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
| **Required** |  |
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
| **Required** |  |
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
| **Repeatable** |  |
| **Constraints** | Controlled vocabulary? |
| **Examples** |  |
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