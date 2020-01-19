# GeographicOrigin

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Type** | Dimension |
| **Hierarchy** | Yes |
| **Range** | no |
| **Potential standards/vocabularies/ontologies to adopt** |  |
| **Notes** | Hierarchy can be flattened as per DwC |

## GeographicOrigin (class)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Parent** | CollectionDescription |
| **Definition** | The geographic location from which objects associated with the CollectionDescription were collected. |
| **Repeatable** | Yes |
| **Relationships** | CollectionDescription (1 to many) <-> GeographicOrigin (0 to many) |
| **Potential standards/vocabularies/ontologies to adopt** | |
| **Notes** |  |

### locationID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** | dwc:locationID |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#locationID |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### higherGeographyID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** | dwc:higherGeographyID |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#higherGeographyID |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### higherGeography (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A list (concatenated and separated) of geographic names less specific than the information captured in the locality term. |
| **Dimension** |  |
| **Existing property** | dwc:higherGeography |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#higherGeography |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### continent (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the continent in which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:continent |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#continent |
| **Format** | text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### waterBody (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the water body in which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:waterBody |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#waterBody |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### islandGroup (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the island group in which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:islandGroup |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#islandGroup |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### island (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the island on or near which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:island |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#island |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### country (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the country or major administrative unit in which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:country |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#country |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### countryCode (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The ISO 3166-1-alpha-2 standard code for the country in which the GeographicOrigin occurs.
| **Dimension** |  |
| **Existing property** | dwc:countryCode |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#countryCode |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### stateProvince (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the next smaller administrative region than country (state, province, canton, department, region, etc.) in which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:stateProvince |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#stateProvince |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### county (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The full, unabbreviated name of the next smaller administrative region than stateProvince (county, shire, department, etc.) in which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:county |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#county |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### municipality (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The full, unabbreviated name of the next smaller administrative region than county (city, municipality, etc.) in which the GeographicOrigin occurs. |
| **Dimension** |  |
| **Existing property** | dwc:municipality |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#municipality |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### locality (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The specific description of the place. Less specific geographic information can be provided in other geographic terms (higherGeography, continent, country, stateProvince, county, municipality, waterBody, island, islandGroup). |
| **Dimension** |  |
| **Existing property** | dwc:locality |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#locality |
| **Format** | Text |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### verbatimLocality (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** |  |
| **Dimension** |  |
| **Existing property** | dwc:verbatimLocality |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#verbatimLocality |
| **Format** |  |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |
