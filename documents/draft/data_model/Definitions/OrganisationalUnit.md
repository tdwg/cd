# OrganisationalUnit

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Dimension |
| **Hierarchy** | Yes |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** | Used for building an organisational hierarchy at sub-institution level. Separate from the Institution dimension at present to allow a collection description to have an institution directly attached without having to navigate a hierarachy. However, the two dimensions could conceivably be merged into a single hierarchy, treating institution as a type/level of organisational unit. |

## OrganisationalUnit (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescription |
| **Definition** | An organisational unit within an institutional hierarchy |
| **Repeatable** |  |
| **Relationships** | CollectionDescription (1 to many) <-> OrganisationalUnit (0 to 1) |
| **Potential standards/vocabularies/ontologies to adopt** | AIISO (http://vocab.org/aiiso/) ; FOAF (http://xmlns.com/foaf/0.1/) |
| **Notes** |  |

### organisationalUnitName (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Official name of the organisational unit in the local language. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2001/vcard-rdf/3.0#Orgname |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### alternativeName (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Alternative name for the unit in English, if the official name is not in English. |
| **Dimension** |  |
| **Existing property** | dc:alternative |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/terms/alternative |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |


### description (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Description of the organisational unit, suitable for a general audience. |
| **Dimension** |  |
| **Existing property** | dc:description |
| **Existing class** |  |
| **Existing property identifier** | http://purl.org/dc/elements/1.1/description |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### organisationalUnitType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The type or level of organisational unit |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Department; Division; Section |
| **Notes** |  |

### immediateParentID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | ID of the parent organisational unit |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |

### parentInstitutionID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | ID of the institution to which the organisational unit belongs |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** |  |
| **Repeatable** | Yes |
| **Constraints** |  |
| **Examples** |  |

## OrganisationalUnitIdentifier (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | OrganisationalUnit |
| **Definition** |  |
| **Repeatable** | Yes |
| **Relationships** | OrganisationalUnit (1 to many) <-> OrganisationalUnitIdentifier (1 to many) |
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
| **Examples** |  |
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
| **Examples** |  |
| **Notes** |  |

### identifier (property)

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

## OrganisationalUnitAddress (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | OrganisationalUnit |
| **Definition** | A physical postal address for an organisational unit |
| **Repeatable** | Yes |
| **Relationships** | OrganisationalUnit (1 to many) <-> OrganisationalUnitAddress (1 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | vCard (http://www.w3.org/TR/vcard-rdf/) |
| **Notes** |  |

### country (property)

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

### stateOrCounty (property)

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

### city (property)

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