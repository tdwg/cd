# Person

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Class |
| **Hierarchy** | no |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** | This is an attempt to merge CollectionContact and Collector |

## Person (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** |  |
| **Definition** | Person associated with the CollectionDescription |
| **Repeatable** |  |
| **Relationships** | CollectionDescription (1) <-> Person (0 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | vCard https://www.w3.org/TR/vcard-rdf/ |
| **Notes** |  |

###  personID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Unique identifier of the person described |
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

### familyName (propery)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Family name of the person described |
| **Dimension** |  |
| **Existing property** | vcard:family-name |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#family-name |
| **Format** | String |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### personGivenName (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Given name of the person described |
| **Dimension** |  |
| **Existing property** | vcard:given-name |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#given-name |
| **Format** | String |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### personHonorificPrefix (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The honorific prefix of the name associated with the person described |
| **Dimension** |  |
| **Existing property** | vcard:given-name |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#honorific-prefix |
| **Format** | String |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### personRole (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The role of person described |
| **Dimension** |  |
| **Existing property** | vcard:role |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#role |
| **Format** | String |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Collector, Director, Collection manager, scientist |
| **Notes** |  |

### personExpertise (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Expertise of the person described |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | String |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Taxonomy, Rubiaceae, Management... |
| **Notes** |  |

### personStatus (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Status of the person described |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Controlled vocabulary |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Active, retired, deceased |
| **Notes** |  |

### personStatusStartDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | start date of the status of the person |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Date |
| **Required** | No |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Active, retired, deceased |
| **Notes** |  |

### personStatusEndDate (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | end date of the status of the person |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** |  |
| **Format** | Date |
| **Required** | No |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Active, retired, deceased |
| **Notes** |  |

### country (propery)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | country of residence of the person |
| **Dimension** |  |
| **Existing property** | vcard:country-name |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#country-name |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### region (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The region (e.g. state or province) associated with the address of the person |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** | vcard:region |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#region |
| **Format** | Date |
| **Required** | No |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Active, retired, deceased |
| **Notes** |  |

### city (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The locality (e.g. city or town) associated with the address of the person |
| **Dimension** |  |
| **Existing property** | vcard:locality |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#locality |
| **Format** | Date |
| **Required** | No |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Active, retired, deceased |
| **Notes** |  |

### zipcodeOrPostalcode (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Postal code associated with the address of the person |
| **Dimension** |  |
| **Existing property** |  |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#postal-code |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### street

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | Street address associated with the person |
| **Dimension** |  |
| **Existing property** | vcard:street-address |
| **Existing class** |  |
| **Existing property identifier** | http://www.w3.org/2006/vcard/ns#street-address |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |