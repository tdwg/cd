# List of Latimer Core terms

**Title**
: List of Latimer Core terms

**Date version issued**
: 2021-07-12

**Date created**
: 2021-07-12

**Part of TDWG Standard**
: // Permanent IRI to standard page on tdwg.org

**This version**
: // Persistent link to this version of the termlist doc

**Latest version**
: // Link to the current termlist

**Previous version**
: // Persistent link to the last version of the termlist doc

**Abstract**
: Latimer Core (LC) is a proposed data standard designed to support the representation, discovery and communication of natural science collections; one LC record describes one entire collection. The classes within the standard aim to allow the high-level representation of any given collection by providing a framework within which the defining characteristics shared by objects in the collection can be described. The creation of collection-level records is hoped to promote visibility and use of items in collections that are otherwise wholly or partially undigitised at a granular level. This document contains a list of attributes of each Latimer Core term, including a documentation name, a specified URI, a recommended English label for user interfaces, a definition, and some ancillary notes.

**Contributors**
: Matt Woodburn, Kate Webbink, Janeen Jones, Sharon Grant, Deborah Paul, Maarten Trekels, Quentin Groom, Sarah Vincent, Gabi Droege, William Ulate, Mike Trizna, Niels Raes, Jutta Buschbom

**Creator**
: TDWG Collection Descriptions (CD) Interest Group

**Bibliographic citation**
: Latimer Core Maintenance Group. 2021. List of Latimer Core terms. Biodiversity Information Standards (TDWG). <Persistent link to this version of the termlist doc>


## 1 Introduction

### 1.1 Status of the content of this document
// content to go here: which sections of the header page are normative, which ones are not

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.3 Categories of terms
// content to go here: description of different types of terms. Could ignore specific classes for now (they're listed in the next section + terms) and discuss more generically the purpose/diff between types of classes: 
- generic classes (Identifier, ResourceRelationship, measurementOrFact, person, ..?)
- collection property classes (anything that relates to the characteristics of the objects or collection: aka values that are unlikely to change unless the items in the collection change - collector people, temporal coverage, objectgroup, geological context, chronometric age, taxon...)
- contextual property classes (characteristics of the collection that might change independently of the objects in the collection: organizational unit, storage location, licenses, collection history, contact person, specimen identifier system...) 
- administrative/scheme classes (anything to help interpret/work with the LC record: Record-level, CD scheme, record-creator person?)

## 2 Borrowed Vocabulary
When terms are borrowed from other vocabularies, LC uses the URIs, common abbreviations, and namespace prefixes in use in those vocabularies. The URIs are normative, but abbreviations and namespace prefixes have no impact except as an aid to reading the documentation.

Table 1. Vocabularies from which terms have been borrowed (non-normative)

Note: URIs for terms in most of these namespaces do not dereference to anything.  The authoritative documentation can be obtained by clicking on the vocabulary names in the table.

| Vocabulary | Abbreviation | Namespaces and abbreviations |
|------------|--------------|------------------------------|
| [Darwin Core](https://dwc.tdwg.org/terms/) | DwC         | `dwc: = http://rs.tdwg.org/dwc/terms/`
| [Dublin Core](http://dublincore.org/documents/dcmi-terms/) | DC          | `dc: = http://purl.org/dc/elements/1.1/, dcterms: = http://purl.org/dc/terms/` |
| [Schema.org](https://schema.org/) | Schema      | `schema: =  https://schema.org/version/latest/schemaorg-current-https.rdf` |
| [Resource Description Framework](https://www.w3.org/RDF/) | RDF | `rdf: = http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| [Access to Biological Collection Data](https://abcd.tdwg.org/) | abcd | `abcd: = https://abcd.tdwg.org/terms/` |


## 3 Namespaces, Prefixes and Term Names
// content to go here - see AC: https://raw.githubusercontent.com/tdwg/ac/master/code/termlist-header.md
