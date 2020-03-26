# RelatedDatasetIdentifier

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Class |
| **Hierarchy** | no |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** |  |

## RelatedDatasetIdentifier (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescription |
| **Definition** | A persistent identifier, in the form of a link or reference, which represents a dataset containing data that are relevant to the collection and the objects within it. |
| **Repeatable** | yes |
| **Relationships** | CollectionDescription (1 to many) <-> RelatedDatasetIdentifier (0 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | DataCite metadata schema (https://schema.datacite.org/meta/kernel-4.3/) |
| **Notes** |  |

### datasetIdentifier (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A persistent identifier that identifies a resource. |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 10.5072/example-full |
| **Notes** | This can be aligned with the identifier term in the DataCite metadata schema (https://schema.datacite.org/meta/kernel-4.3/) |

### datasetIdentifierType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The type of identifier or scheme to which the identifier belongs. |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | DOI |
| **Notes** | This can be aligned with the identifierType term in the DataCite metadata schema (https://schema.datacite.org/meta/kernel-4.3/) |