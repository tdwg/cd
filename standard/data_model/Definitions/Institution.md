# Institution

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Dimension |
| **Hierarchy** | no |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** |  |

## Institution (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescription |
| **Definition** | The institution that maintains the collection |
| **Repeatable** | Yes |
| **Relationships** | CollectionDescription (1 to many) <-> Institution (0 to 1) |
| **Potential standards/vocabularies/ontologies to adopt** | "AIISO (http://vocab.org/aiiso/), FOAF (http://xmlns.com/foaf/0.1/)" |
| **Notes** |  |

### institutionName (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Official name of the Institution in the local language. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2001/vcard-rdf/3.0#Orgname |
| **Format** | Text |
| **Required** | yes |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Natural History Museum, London; Agentschap Plantentuin Meise; Florida State University |
| **Notes** |  |

### alternativeName (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Alternative name for the institution in English, if the official name is not in English. |
| **Dimension** |  |
| **Existing property** | dc:alternative |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/alternative |
| **Format** | Text |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Meise Botanic Garden |
| **Notes** |  |

### institutionAcronym (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Institutional acronym preferred by the institution. This will not necessarily be unique across global institutions. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | SMNS |
| **Notes** |  |

### description (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Description of institution, suitable for a general audience. |
| **Dimension** |  |
| **Existing property** | dc:description |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/elements/1.1/description |
| **Format** |  |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | From NCD |

### institutionType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Picklist keyword describing the primary activity or purpose of an organisation or entity that holds or uses collections. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | From NCD |

### parentInstitutionOrNetwork (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Name, acronym, identifier or code of parent institution or network(s) |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** |  |
| **Repeatable** | Yes |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### websiteURL (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | URL of the institution's main website |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** | Valid URL |
| **Examples** |  http://col.smns-bw.org/|
| **Notes** |  |

## InstitutionIdentifier (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | Institution |
| **Definition** |  |
| **Repeatable** | Yes |
| **Relationships** | Institution (1 to many) <-> InstitutionIdentifier (1 to many) |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** |  |

### type (property)

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
| **Examples** | GBIFPublisherGUID; GRBioID; GRIDIdentifier; VIAFIdentifier |
| **Notes** |  |

### source (property)

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
| **Examples** | GBIF; GRID; GRBio; VIAF |
| **Notes** |  |

### identifier (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The unique identifier of the institution from the source |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** | yes |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | 99ea0c90-61e5-11dc-a64c-b8a03c50a862; http://biocol.org/urn:lsid:biocol.org:col:34840 |
| **Notes** |  |

## InstitutionAddress (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | Institution |
| **Definition** | A physical postal address for an institution |
| **Repeatable** | Yes |
| **Relationships** | Institution (1 to many) <-> InstitutionAddress (1 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | vCard (http://www.w3.org/TR/vcard-rdf/) |
| **Notes** |  |

### country (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The country in which the institution is located |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | yes |
| **Repeatable** | Single |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### stateOrCounty (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** | Single |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### city (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** | Single |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### zipcodeOrPostcode (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | Single |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### street (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the street or road on which the postal address of the institution is located |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | no |
| **Repeatable** | Single |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |
