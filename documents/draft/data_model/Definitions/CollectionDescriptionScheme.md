# CollectionDescription 

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Class |
| **Hierarchy** | no |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** |  |

## CollectionDescriptionScheme (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | NA |
| **Definition** | A mechanism to group CollectionDescription objects, constrain their scope within the wider standards, and define rules to which they must adhere for interoperability. |
| **Repeatable** |  |
| **Relationships** | CollectionDescription (1 to many) <-> CollectionDescriptionScheme (1) |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### schemeID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Unique identifier for the scheme, enabling conformant CollectionDescription records to be identified and metrics aggregated according to the scheme definitions |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | GUID? |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### schemeName (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Short descriptive name for the scheme |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### distinctObjects (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Flag to designate that no physical object should be described by more than one CollectionDescription within the scheme. Important for aggregating and reporting on metrics such as object counts. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Boolean |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

## schemeDimension (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescriptionScheme |
| **Definition** | Dimension used by the scheme and rules relating to its application. |
| **Repeatable** | Yes |
| **Relationships** | CollectionDescriptionScheme (1) <-> SchemeDimension (1 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### dimension (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The dimension's term within the collection descriptions standard. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | GeographicOrigin; Institution; GeologicalTimeRange |
| **Notes** |  |

### isMandatory (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Flag to designate whether it is mandatory or optional for every collection description within the scheme to include the dimension. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Boolean |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### isRepeatable (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Flag to designate whether more than one record for the dimension can be attached to the CollectionDescription. If so, it may not be possible to aggregate metrics for that dimension. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Boolean |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

## schemeMetric (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescriptionScheme |
| **Definition** | Metric used by the scheme and rules relating to its application. |
| **Repeatable** | Yes |
| **Relationships** | CollectionDescriptionScheme (1) <-> SchemeMetric (1 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### metricName (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The metric's term within the collection descriptions standard. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | ObjectQuantity; TaxonQuantity |
| **Notes** |  |

### isMandatory (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Flag to designate whether it is mandatory for every collection description within the scheme to have a value for the metric. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Boolean |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |