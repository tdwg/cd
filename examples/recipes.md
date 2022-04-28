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
  - Identifier 
  - OrganisationalUnit 
  - Person 
  - PersonRole 


**Example:** [FMNH Institution Record](https://docs.google.com/spreadsheets/d/1ceUOYz6w6wxW6m_Lepj2RIXpTl5pZULD-Er71i4_3J0/edit#gid=1389433917) ("FMNH_Institution" tab of google sheet)

As a flat CSV:

Term | Class |	Value
---|---|---
organisationalUnitName | OrganisationalUnit	| Field Museum of Natural History
organisationalUnitType | OrganisationalUnit |	Institution
organisationalUnitParentInstitutionID | OrganisationalUnit | urn:lsid:biocol.org:col:34795
addressLocality	| OrganisationalUnit.Address	| Chicago
addressCountry	| OrganisationalUnit.Address	| USA
addressRegion	| OrganisationalUnit.Address	| IL
streetAddress	| OrganisationalUnit.Address	| 1400 S DuSable Lake Shore Dr.
postalCode | OrganisationalUnit.Address	| 60605
addressType	| OrganisationalUnit.Address | Physical
temporalCoverageStartDate	| OrganisationalUnit.TemporalCoverage	| 1894-06-02
temporalCoverageType | OrganisationalUnit.TemporalCoverage | Establishment time range
continent	| OrganisationalUnit.GeographicOrigin	| worldwide
identifierSource	| OrganisationalUnit.Identifier	| GrSciColl
identifier	| OrganisationalUnit.Identifier	| urn:uuid:ea4f0640-ef20-40aa-b359-166f07c7492a
identifierType	| OrganisationalUnit.Identifier	| UUID
identfierSource	| OrganisationalUnit.PersonRole_1.Person.Identifier	| ORCiD
identifier	| OrganisationalUnit.PersonRole_1.Person.Identifier | https://orcid.org/0000-0001-8777-7143
identifierType	| OrganisationalUnit.PersonRole_1.Person.Identifier	| URL
role	| OrganisationalUnit.PersonRole_1	| CTO
fullName	| OrganisationalUnit.PersonRole_1.Person	| Rob Zschernitz
role	| OrganisationalUnit.PersonRole_2	| CEO
fullName	| OrganisationalUnit.PersonRole_2.Person	| Julian Siggers

Or as nested JSON:
```
{
  "OrganisationalUnit": {
    "ltc:organisationalUnitName": "Field Museum of Natural History",
    "ltc:organisationalUnitType": "Institution",
    "ltc:organisationalUnitParentInstitutionID": "urn:lsid:biocol.org:col:34795",
    "Address": {
      "ltc:addressLocality": "Chicago",
      "ltc:addressCountry": "USA",
      "ltc:addressRegion": "IL",
      "ltc:streetAddress": "1400 S DuSable Lake Shore Dr.",
      "ltc:postalCode": "60605",
      "ltc:addressType": "Physical"
    },
    "CollectionStatusHistory": {
      "ltc:status": "open",
      "ltc:statusType": "Organizational"
    },
    "GeographicOrigin": {
      "dwc:continent": worldwide
    },
    "Identifier": {
      "ltc:identfierSource": "GrSciColl",
      "ltc:identfier": "urn:uuid:ea4f0640-ef20-40aa-b359-166f07c7492a",
      "ltc:identfierType": "UUID"
    },
    "PersonRole": {
      "ltc:role": "CTO",
      "Person": {
        "ltc:fullName": "Rob Zschernitz",
        "Identifier": {
          "ltc:identfierSource": "ORCiD",
          "ltc:identfier": "https://orcid.org/0000-0001-8777-7143",
          "ltc:identfierType": "URL"
        }
      },
      "ltc:role": "CEO",
      "Person": {
        "ltc:fullName": "Julian Siggers"
      }
    }
  }
}
```

## A record for a collection or department within an institution

- **Example**: [FMNH Collection Record](https://docs.google.com/spreadsheets/d/1ceUOYz6w6wxW6m_Lepj2RIXpTl5pZULD-Er71i4_3J0/edit#gid=0&range=A1) ("FMNH_Collection" tab of google sheet)


## A record for an accession within an institution

- **Example**: [FMNH Meek Accession](https://docs.google.com/spreadsheets/d/1ceUOYz6w6wxW6m_Lepj2RIXpTl5pZULD-Er71i4_3J0/edit#gid=1952584578&range=A2) ("FMNH_Accession_Meek" tab of google sheet)

- **Example** [FMNH Carpenter Accession](https://docs.google.com/spreadsheets/d/1ceUOYz6w6wxW6m_Lepj2RIXpTl5pZULD-Er71i4_3J0/edit#gid=1102807335&range=A1) ("FMNH_Accession_Carpenter" tab of google sheet)



# Alternate ways to structure CSV Latimer Core records

## A record as a set of relational tables (separate CSVs or multi-tab google sheet)

- Example: [NHM Challenger Expedition](https://docs.google.com/spreadsheets/d/1IxHdpMJyn_TZaTlIKw_jUSlz6uZZ_ApTi5QL9i0kvRg/edit#gid=1755256505) 

- Example: [FMNH Carpenter Accession](https://docs.google.com/spreadsheets/d/10OXg7Vp750P6wIhtWlx2TnuZ8MfaeTK6QnlnDl4wYsY/edit#gid=0) 

The classes and terms could alternatively be set up as a group of relational tables or CSVs like so:
#### CSV/Table 1: ObjectGroup:

ObjectGroup_key | ltc:discipline | ltc:description | ltc:collectionName
---|---|---|---
1 | Taxonomy \| Zoology | Established in 1894, The Field Museum fish collection now contains [...] | Fishes Collection


#### CSV/Table 2: ObjectGroup.Identifier

ObjectGroup_key | Identifier_key | ltc:identifierSource | ltc:identifier | ltc:identifierType 
---|---|---|---|---
1 | 1 | Collection database | https://collections-zoology.fieldmuseum.org/Fishes | URL
1 | 2 | GrSciColl | http://grscicoll.org/institutional-collection/fish-collections | GRSCICOLL URI


### Nested JSON

