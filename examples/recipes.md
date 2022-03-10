# Recipes & Examples for Latimer Core records [DRAFT]

Latimer Core can be used to describe collections at a variety of levels -- for instance, at a more finely detailed expeditions or accession-levels, or at more general departmental or institution-levels.  Or both nested within a single record, if that isn't too horrifying.
Each of the sections below is meant to illustrate an example of a different Basis of Scheme (`ltc:basisOfScheme`) value.

## Common to all Latimer Core record-typesThe classes and terms are useful for documenting any Latimer Core record-type
- RecordLevel Class
- ObjectGroup Class
- 

## A record for a whole institution 
These classes and terms are useful for documenting an institution:
- Address Class:
- CollectionHistory Class
- ContactDetail Class
- GeographicOrigin Class
- Identifier Class
- OrganisationalUnit Class
- Person Class
- PersonRole Class


Term | Class |	Value
-|-|-
organisationalUnitName | OrganisationalUnit	| Field Museum of Natural History
organisationalUnitType | OrganisationalUnit |	Institution
organisationalUnitParentInstitutionID	OrganisationalUnit	urn:lsid:biocol.org:col:34795
addressLocality	OrganisationalUnit.Address	Chicago
addrissCountry	OrganisationalUnit.Address	USA
addressRegion	OrganisationalUnit.Address	IL
streetAddress	OrganisationalUnit.Address	1400 S DuSable Lake Shore Dr.
postalCode	OrganisationalUnit.Address	60605
addressType	OrganisationalUnit.Address	Physical
status	OrganisationalUnit.CollectionStatusHistory	open
statusType	OrganisationalUnit.CollectionStatusHistory	Organizational
continent	OrganisationalUnit.GeographicOrigin	worldwide
identifierSource	OrganisationalUnit.Identifier	GrSciColl
identifier	OrganisationalUnit.Identifier	urn:uuid:ea4f0640-ef20-40aa-b359-166f07c7492a
identifierType	OrganisationalUnit.Identifier	UUID
identfierSource	OrganisationalUnit.PersonRole_1.Person.Identifier	ORCid
identifier	OrganisationalUnit.PersonRole_1.Person.Identifier	https://orcid.org/0000-0001-8777-7143
identifierType	OrganisationalUnit.PersonRole_1.Person.Identifier	URL
role	OrganisationalUnit.PersonRole_1	CTO
fullName	OrganisationalUnit.PersonRole_1.Person	Rob Zschernitz
role	OrganisationalUnit.PersonRole_2	CEO
fullName	OrganisationalUnit.PersonRole_2.Person	Julian Siggers

In CSV or table-form, the classes and terms could be structured as a group of CSVs or tables like so:
- CSV/Table 1: OrganizationalUnit
- CSV/Table 2: Org-Address


## A record for a department within an institution

### A standalone record for a department that references a separate parent institution record

### A nested record that includes a department as well as its parent institution

## A collection
