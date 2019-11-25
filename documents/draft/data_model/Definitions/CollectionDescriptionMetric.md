# CollectionDesctriptionMetric

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Metric |
| **Hierarchy** | no |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** | May be a better model to remove the CollectionDesctriptionMetric class, and attach these properties and subclasses directly to the CollectionDescription class. |

## CollectionDescriptionMetric (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** |  |
| **Definition** |  |
| **Repeatable** | no |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** | Might be neater to wrap the storage metrics up as a subclass rather than properties of CollectionDescriptionMetric (or CollectionDescription), despite the 1:1 relationship |

### storageVolume (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Numeric |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### storageVolumeUnit (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |

### storageVolumeConfidence (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Percentage |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 10% |
| **Notes** |  |

### storageVolumeMethod (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Estimate; Precise count; Minimum; Maximum |
| **Notes** |  |

### storageFootprint (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Numeric |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### storageFootprintUnit (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |

### storageFootprintConfidence (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Percentage |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 5% |
| **Notes** |  |

### storageFootprintMethod (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Estimate; Precise count; Minimum; Maximum |
| **Notes** |  |

## ObjectQuantity (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescriptionMetric |
| **Definition** | Metric for recording counts or estimates of the quantity of objects described by the CollectionDescription. |
| **Repeatable** | Yes |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** | Should support multiple quantity metrics of different types for physical objects within the CollectionDescription. The objectType controlled vocabulary is key for constraining these definitions and making the figures interoperable between CollectionDescription records and schemes. |

### objectType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The type of collection object that is being quantified. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Organism; Curatorial object; Lot; Imaged object; Type specimen |
| **Notes** |  |

### quantity (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The quantity of objects described by the CollectionDescription, as defined by the objectType. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Integer |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 20000 |
| **Notes** | Type of object counted is defined by the ObjectType defined for the CollectionDescription e.g. jar, slide, whole organism |

### confidence (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A measure (precise or approximate) of the percentage error on the estimated object count. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Percentage |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 5% |
| **Notes** | Application will be influenced by the objectQuantityMethod |

### quantityMethod (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The method used to count the objects represented by the CollectionDescription. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Estimate; Precise count; Minimum; Maximum |
| **Notes** |  |

## TaxonQuantity (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescriptionMetric |
| **Definition** | Metric for recording counts or estimates of the number of taxa represented by the CollectionDescription. |
| **Repeatable** | Yes |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### taxonRank (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The taxonomic rank that is being quantified. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Kingdom; Order; Genus; Species |
| **Notes** |  |

### taxonQuantity (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The quantity of taxa that are represented by the objects represented by the CollectionDescription. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Integer |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 10000 |
| **Notes** |  |

### taxonQuantityConfidence (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A measure (precise or approximate) of the percentage error on the estimated taxon count. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | percentage |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 5% |
| **Notes** |  |

### taxonQuantityMethod (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The method used to count the taxa represented by the CollectionDescription. |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Estimate; Precise count; Minimum; Maximum |
| **Notes** |  |

## ObjectDigitalRecordMetric (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescriptionMetric |
| **Definition** |  |
| **Repeatable** | Yes |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### digitalRecordType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Type or level of digital record with reference to the object(s) that it describes |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** | Yes |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Object; Lot; Sample |
| **Notes** |  |

### digitalRecordQuantity (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The quantity of digital records of the defined digitalRecordType that represent the objects within the Collection Description |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Integer |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 26; 264; 99,657 |
| **Notes** |  |

## DigitizationLevelAssessment (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | ObjectDigitalRecordMetric |
| **Definition** | Description of the quantity of object-level digital records related to the CollectionDescription at a defined level of completeness |
| **Repeatable** | Yes |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### digitizationLevel (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Code or name for the digitization completeness level |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | Level 1; A; Inventory; Catalogued; MIDS1 |
| **Notes** |  |

### digitizationLevelDefinition (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Definition of the digitization completeness level |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** | A basic record of specimen information, largely based on current practices, enabling similar discovery capabilities on-line as researchers and curators would have by more traditional means. |

### digitizationLevelQuantity (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The quantity of object-level digital records that conform to the DigitizationLevel |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Numeric |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 140; 99; 200,000 |
| **Notes** |  |

### digitizationLevelQuantityType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The type of quantification system used for the quantity of digital records at the defined digitization completeness level |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Units; Percentage |
| **Notes** |  |

### digitizationLevelSource (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Indicator of whether the DigitizationLevel data are calculated from the digital records, or manually estimated |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Calculated; Reported |
| **Notes** |  |

## DataQualityAssessment (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | ObjectDigitalRecordMetric |
| **Definition** | A quantification of digital records that meet a defined data quality or completeness criterion |
| **Repeatable** | Yes |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### dataQualityDefinition (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Definition of the digitization quality indicator |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | Georeferenced; Verified; Linked to taxonomic authority |
| **Notes** |  |

### dataQualityQuantity (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The quantity of object-level digital records that conform to the DigitizationQualityAssessment |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Numeric |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | 140; 99; 200,000 |
| **Notes** |  |

### dataQualityQuantityType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The type of quantification system used for the quantity of digital records that conform to the DigitizationQualityAssessment |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Units; Percentage |
| **Notes** |  |

### dataQualitySource (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Indicator of whether the DigitizationQualityAssessment data are calculated from the digital records, or manually estimated |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** | Calculated; Reported |
| **Notes** |  |

## DigitalMediaAssetQuantity (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | ObjectDigitalRecordMetric |
| **Definition** |  |
| **Repeatable** | Yes |
| **Relationships** |  |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### digitalAssetType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The type of digital Asset (i.e., electronic file) related to the CollectionDescription |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |

### digitalAssetQuantity (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The number of digital Asset objects of the defined digitalAssetType associated with the CollectionDescription |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Numeric |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### digitalAssetQuantityType (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Type of quantification system used for digitalAssetQuantity |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Text |
| **Required** |  |
| **Repeatable** | no |
| **Constraints** | Controlled vocabulary |
| **Examples** |  |
| **Notes** |  |