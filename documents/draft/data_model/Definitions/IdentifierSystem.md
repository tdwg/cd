# IdentifierSystem

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Dimension |
| **Hierarchy** | no |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** |  |

## IdentifierSystem (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescription |
| **Definition** | A locally unique identifer system used within a collection to identify a specimen |
| **Repeatable** |  |
| **Relationships** | CollectionDescription (1) <-> IdentifierSystem (0 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### readingFormat (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The means by which the identifer can be read by machine |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | controlled vocabulary |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | barcode, RDF Tag, printed number |
| **Notes** |  |

### codeType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | controlled vocabulary |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | number, character, alphanumeric |
| **Notes** |  |

### codeFormat (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The official name of the machine readable identifier |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | controlled vocabulary |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | QR Code, EAN-13, Code 128, Data Matrix |
| **Notes** |  |

### regex (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A regular expression that can be used to confirm that an identifier conforms to that institutions standard |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | BR[0-9]{13}V? |
| **Notes** |  |

### startDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The date at which the identifier was first used in the institution |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Date |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** | ISO 8601 date format, resolved to day, month or year |
| **Examples** |  |
| **Notes** |  |

### endDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The last date at which the identifier was used in the institution |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Date |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** | ISO 8601 date format, resolved to day, month or year |
| **Examples** |  |
| **Notes** |  |

### cardinality (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | An indication of whether identifiers are linked to single specimen, or may cover multiple specimens within the collection. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |
