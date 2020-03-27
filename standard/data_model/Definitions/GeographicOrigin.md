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
| **Definition** | An identifier for the set of location information (data associated with dcterms:Location). May be a global unique identifier or an identifier specific to the data set. |
| **Dimension** |  |
| **Existing property** | dwc:locationID |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#locationID |
| **Format** |  |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | 	https://opencontext.org/subjects/768A875F-E205-4D0B-DE55-BAB7598D0FD1 |
| **Notes** |  |

### higherGeographyID (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | An identifier for the geographic region within which the Location occurred. |
| **Dimension** |  |
| **Existing property** | dwc:higherGeographyID |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#higherGeographyID |
| **Format** |  |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | http://vocab.getty.edu/tgn/1002002 (Antártida e Islas del Atlántico Sur, Territorio Nacional de la Tierra del Fuego, Argentina). |
| **Notes** | Recommended best practice is to use a persistent identifier from a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |

### higherGeography (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | A list (concatenated and separated) of geographic names less specific than the information captured in the locality term. |
| **Dimension** |  |
| **Existing property** | dwc:higherGeography |
| **Existing class** | Collection Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#higherGeography |
| **Format** |  |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### continent (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the continent in which the Location occurs. |
| **Dimension** |  |
| **Existing property** | dwc:continent |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#continent |
| **Format** | controlled vocabulary |
| **Required** | no |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | Africa, Antarctica, Asia, Europe, North America, Oceania, South America |
| **Notes** | This terms refers to the continent from which the collection originated. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. --> http://www.getty.edu/vow/TGNHierarchy?find=&place=&nation=&english=Y&subjectid=7029392 |

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
| **Format** |  |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |

### islandGroup (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the island group in which the Location occurs. |
| **Dimension** |  |
| **Existing property** | dwc:islandGroup |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#islandGroup |
| **Format** | controlled vocabulary |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Alexander Archipelago, Archipiélago Diego Ramírez, Seychelles |
| **Notes** | This terms refers to the island group from which the collection originated. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. --> http://www.getty.edu/vow/TGNHierarchy?find=&place=&nation=&english=Y&subjectid=7029392 |

### island (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the island on or near which the Location occurs. |
| **Dimension** |  |
| **Existing property** | dwc:island |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#island |
| **Format** | controlled vocabulary |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Nosy Be, Bikini Atoll, Vancouver, Viti Levu, Zanzibar |
| **Notes** | This terms refers to the island from which the collection originated. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. --> http://www.getty.edu/vow/TGNHierarchy?find=&place=&nation=&english=Y&subjectid=7029392 |

### country (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The name of the country or major administrative unit in which the Location occurs. |
| **Dimension** |  |
| **Existing property** | dwc:country |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#country |
| **Format** | controlled vocabulary |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Angola, Denmark, Colombia, España |
| **Notes** | This terms refers to the country from which the collection items were collected. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. --> http://www.getty.edu/vow/TGNHierarchy?find=&place=&nation=&english=Y&subjectid=7029392 |

### countryCode (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The standard code for the country in which the Location occurs.
| **Dimension** |  |
| **Existing property** | dwc:countryCode |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#countryCode |
| **Format** | controlled vocabulary |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | AR, SV, CN |
| **Notes** | This terms refers to the code of the country from which the collection originated. Recommended best practice is to use an ISO 3166-1-alpha-2 country code. |

### stateProvince (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | 	The name of the next smaller administrative region than country (state, province, canton, department, region, etc.) in which the Location occurs. |
| **Dimension** |  |
| **Existing property** | dwc:stateProvince |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#stateProvince |
| **Format** | controlled vocabulary |
| **Required** |  |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Montana, Minas Gerais, Córdoba |
| **Notes** | Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |

### county (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The full, unabbreviated name of the next smaller administrative region than stateProvince (county, shire, department, etc.) in which the Location occurs. |
| **Dimension** |  |
| **Existing property** | dwc:county |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#county |
| **Format** | Text |
| **Required** |  |
| **Format** | controlled vocabulary |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Missoula, Los Lagos, Mataró |
| **Notes** | This terms refers to the county from which the collection originated. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. --> http://www.getty.edu/vow/TGNHierarchy?find=&place=&nation=&english=Y&subjectid=7029392 |

### municipality (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The full, unabbreviated name of the next smaller administrative region than county (city, municipality, etc.) in which the Location occurs. Do not use this term for a nearby named place that does not contain the actual location. |
| **Dimension** |  |
| **Existing property** | dwc:municipality |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#municipality |
| **Format** | controlled vocabulary |
| **Required** | no |
| **Repeatable** | no |
| **Constraints** |  |
| **Examples** | Holzminden, Araçatuba, Ga-Segonyana |
| **Notes** | Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |

### locality (property)

| <!-- --> | <!-- --> |
| ---- | ---- |
| **Definition** | The specific description of the place. Less specific geographic information can be provided in other geographic terms (higherGeography, continent, country, stateProvince, county, municipality, waterBody, island, islandGroup). This term may contain information modified from the original to correct perceived errors or standardize the description. |
| **Dimension** |  |
| **Existing property** | dwc:locality |
| **Existing class** | Location |
| **Existing property identifier** | http://rs.tdwg.org/dwc/terms/#locality |
| **Format** | Text |
| **Required** |  |
| **Format** |  |
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** | Bariloche, 25 km NNE via Ruta Nacional 40 (=Ruta 237). |
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
| **Required** | no |
| **Repeatable** |  |
| **Constraints** |  |
| **Examples** |  |
| **Notes** |  |
