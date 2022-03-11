# Recipes & Examples for Latimer Core records [DRAFT]

Latimer Core can be used to describe collections at a variety of levels -- for instance, at a more finely detailed expeditions or accession-levels, or at more general departmental or institution-levels.  Or both nested within a single record, if that isn't too horrifying.
Each of the sections below is meant to illustrate an example of a different Basis of Scheme (`ltc:basisOfScheme`) value.

## Common to all Latimer Core record-types
These classes and terms are useful for documenting any Latimer Core record-type
- RecordLevel
- ObjectGroup
- Identifier
- Person
- Address

## A record for a whole institution 
These classes and terms are useful for documenting an institution:
- Address
- CollectionHistory
- ContactDetail
- GeographicOrigin 
- Identifier Class
- OrganisationalUnit Class
- Person Class
- PersonRole Class

### Example: [FMNH Institution Record](https://docs.google.com/spreadsheets/d/1ceUOYz6w6wxW6m_Lepj2RIXpTl5pZULD-Er71i4_3J0/edit#gid=1389433917)

Term | Class |	Value
---|---|---
organisationalUnitName | OrganisationalUnit	| Field Museum of Natural History
organisationalUnitType | OrganisationalUnit |	Institution
organisationalUnitParentInstitutionID | OrganisationalUnit | urn:lsid:biocol.org:col:34795
addressLocality	| OrganisationalUnit.Address	| Chicago
addrissCountry	| OrganisationalUnit.Address	| USA
addressRegion	| OrganisationalUnit.Address	| IL
streetAddress	| OrganisationalUnit.Address	| 1400 S DuSable Lake Shore Dr.
postalCode | OrganisationalUnit.Address	| 60605
addressType	| OrganisationalUnit.Address | Physical
status	| OrganisationalUnit.CollectionStatusHistory	| open
statusType	| OrganisationalUnit.CollectionStatusHistory	| Organizational
continent	| OrganisationalUnit.GeographicOrigin	| worldwide
identifierSource	| OrganisationalUnit.Identifier	| GrSciColl
identifier	| OrganisationalUnit.Identifier	| urn:uuid:ea4f0640-ef20-40aa-b359-166f07c7492a
identifierType	| OrganisationalUnit.Identifier	| UUID
identfierSource	| OrganisationalUnit.PersonRole_1.Person.Identifier	| ORCid
identifier	| OrganisationalUnit.PersonRole_1.Person.Identifier | https://orcid.org/0000-0001-8777-7143
identifierType	| OrganisationalUnit.PersonRole_1.Person.Identifier	| URL
role	| OrganisationalUnit.PersonRole_1	| CTO
fullName	| OrganisationalUnit.PersonRole_1.Person	| Rob Zschernitz
role	| OrganisationalUnit.PersonRole_2	| CEO
fullName	| OrganisationalUnit.PersonRole_2.Person	| Julian Siggers


## A record for a collection or department within an institution

### Example: [FMNH Collection Record](https://docs.google.com/spreadsheets/d/1ceUOYz6w6wxW6m_Lepj2RIXpTl5pZULD-Er71i4_3J0/edit#gid=0&range=A1)

The classes and terms could alternatively be set up as a group of relational tables or CSVs like so:
#### CSV/Table 1: ObjectGroup:

ObjectGroup_key | term | value
---|---|---
1 | ltc:discipline | Taxonomy \| Zoology
1 | ltc:description | Established in 1894, The Field Museum fish collection now contains [...]
1 | ltc:collectionName | Fishes Collection

#### CSV/Table 2: ObjectGroup.Identifier

ObjectGroup_key | Identifier_key | term | value
---|---|---|---
1 | 1 | ltc:identifierSource | Collection database
1 | 1 | ltc:identifier | https://collections-zoology.fieldmuseum.org/Fishes
1 | 1 | ltc:identifierType | URL




