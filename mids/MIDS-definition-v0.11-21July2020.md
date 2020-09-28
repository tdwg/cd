

**Contact: Alex Hardisty, Cardiff University. email: [hardistyar@cardiff.ac.uk](mailto:hardistyar@cardiff.ac.uk) **


<table>
  <tr>
   <td><strong>Version</strong>
   </td>
   <td><strong>Date</strong>
   </td>
   <td><strong>Author</strong>
   </td>
   <td><strong>Changes</strong>
   </td>
  </tr>
  <tr>
   <td>v0.1
   </td>
   <td>27-Nov-2018
   </td>
   <td>E. Haston with RBGE colleagues
   </td>
   <td>Based on various earlier ideas and emails.
   </td>
  </tr>
  <tr>
   <td>v0.2
   </td>
   <td>06-Dec-2018
   </td>
   <td>A. Hardisty
   </td>
   <td>(not distributed)
<p>
Change of name of Complete Record to Comprehensive record.
   </td>
  </tr>
  <tr>
   <td>v0.3
   </td>
   <td>02-Jan-2019
   </td>
   <td>A. Hardisty
   </td>
   <td>Change of name of Comprehensive record to Full record. Modifications to take comments from ICEDIG AHM2 Meise meeting into account. Change to draft 0.n version numbering scheme to make it clear that the specification is a draft in preparation and discussion. Addition of this change history log.
   </td>
  </tr>
  <tr>
   <td>v0.4
   </td>
   <td>04-Jan-2019
   </td>
   <td>E. Haston, A. Hardisty
   </td>
   <td>Added purposes to give rational to each of the three levels. Generalised to encompass a broad range of natural science specimen types.
   </td>
  </tr>
  <tr>
   <td>v0.5
   </td>
   <td>16-Jan-2019
   </td>
   <td>A. Hardisty
   </td>
   <td>Adding information about purpose of MIDS. \
Noting need to align/converge ideas suggested by H. Saarenmaa in MS35 report. \
'Who and when' moved from mandatory column at level 2 to optional column, per suggestion in my email of 04/01/2019. 
   </td>
  </tr>
  <tr>
   <td>V0.6
   </td>
   <td>11-Jun-2019
   </td>
   <td>A. Hardisty
   </td>
   <td>Following CETAF digitization WG meeting, 14 February 2019, Vienna, following changes have been made:
<ul>

<li>Renamed level 2 Partial to level 2 Regular.

<li>Change mandatory to expected.

<li>Take image characteristics stuff out of the specification.

<li>Expanded ‘Locatility information’ to its constituent parts.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>V0.7
   </td>
   <td>04-Jul-2019
   </td>
   <td>
   </td>
   <td>WORD doc inserted into this GoogleDoc.
   </td>
  </tr>
  <tr>
   <td>V0.8
   </td>
   <td>22-Nov-2019
   </td>
   <td>A. Hardisty
   </td>
   <td>Reformatted and structured in the style of a prospective TDWG standard. Begin to add mappings to DwC and ABCD terms.
   </td>
  </tr>
  <tr>
   <td>V0.9
   </td>
   <td>30-Mar-2020
   </td>
   <td>E. Haston
   </td>
   <td>Remove distinction between expected/recommended elements so that at each MIDS level it is clear which elements are expected to be present.
   </td>
  </tr>
  <tr>
   <td>V0.10
   </td>
   <td>12-May-2020
   </td>
   <td>A. Hardisty
   </td>
   <td>Implement changes agreed at meeting, 2<sup>nd</sup> April, including:
<ul>

<li>moving image types/characteristics out of scope and flagging presence/absence of images and other multimedia.

<li>Aligning Geographical region values with CDD expectations.

<li>Resolving many outstanding comments.

<li>Level 0 Catalogue renamed to level 0 Bare.

<li>Implementation Conformance Statement (ICS) proforma checklist added.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>V0.11
   </td>
   <td>21-July-2020
   </td>
   <td>A. Hardisty
   </td>
   <td>Resolve all outstanding comments and suggestions and take into account instructions from review meeting, 17th June 2020; including:
<ul>

<li>Recommendation added (section 4.5.1) for date/time format to use when createdON/modifiedON is unknown or unspecified.

<li>Additional values related to missing information added to table 6/section 4.5.3. 

<li>New sub-section on handling of geographical information added (4.5.2).

<li>PICS proforma updated to match changes throughout.

<li>… ...editing in progress
</li>
</ul>
   </td>
  </tr>
</table>


To do:



*   Go through text carefully to ensure that the public sharing aspect is covered at each place it needs to be.
*   Change name of level 0 to ‘placeholder’ (suggested by MW).
*   PICS proforma to be completed and checked.

Title: Minimum Information about a Digital Specimen (MIDS)

Date version issued: _2020-05-12_

Date created: 2019-11-22

This version: _V0.10_

Latest version: _V0.10_

Previous version: _V0.9_

Abstract: Minimum Information about a Digital Specimen (MIDS) is a specification defining the information elements expected to be present when publishing digitized information about specimens at various levels of digitization. Digital Specimens are digital representations on the Internet of their physical counterparts in natural science collections. The definition of digitization used here is the process of making physical objects digitally available. Levels of digitization represents a simple categorisation of the type and depth of digitization achieved by heterogeneous approaches to digitization.

Contributors: Alex R Hardisty, Wouter Addink, Mathias Dillen, Quentin Groom, Elspeth Haston, Falko Glöckler, Deborah Paul, Mareike Petersen, Hannu Saarenmaa, Anton Güntsch

Creator: _&lt;to be completed>_

Bibliographic citation: _&lt;to be completed>_

Change history: &lt;_to be completed. begins with version 1.0_>



Table of Contents


[TOC]



# 1 Introduction

Minimum Information about a Digital Specimen (MIDS) specifies the information elements expected to be present when providing access to specimens within a digital framework. Digital Specimens are online digital representations of their physical counterparts in natural science collections. The definition of digitization used here is the process of making physical objects digitally available in terms of either data or images. The levels of digitization proposed represent a simple categorisation of the type and depth of digitization achieved by heterogeneous approaches to digitization.

MIDS has multiple aims:



1. To improve the quality of published data by offering clarity to collection owners about the minimum quantity and quality of information they should be publishing to make digital specimen information useful for multiple purposes of teaching and learning, research, etc.;
2. To assist the global effort to digitize natural science collections, estimated to be 3 billion specimens worldwide by providing a structured framework that clarifies the outcomes of digitization and the level of digitization achieved, and assists prioritization of the remaining work;
3. To support and contribute towards assessments of fitness for purpose of data (suitability) for feeding specific types of data processing pipelines; and,
4. To assist researchers to know what information to include in their journal articles about specimens they have used in their research .

MIDS defines what information about a specimen should be available but it does not attach specific value to that information because attaching value depends both upon the information itself and the purpose to which that is put. MIDS does not codify these aspects.

The levels of digitization and their expected information content defined herein, and named as Minimum Information about a Digital Specimen (MIDS) are based on major research and curation requirements put forward by national museums and herbaria.


## 1.1 Audience

This document is intended primarily for those who are responsible for digitizing and sharing data publicly (publishing data) about natural science specimens. It can also be useful to those who are developing applications, tools and workflows related to digitization, and for those reporting to collection management personnel and funding agencies.


## 1.2 RFC 2119 key words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119. [RFC-2119]


## 1.3 Content

This is the only document associated with the specification of Minimum Information about a Digital Specimen (MIDS). Sections are designated as either ‘informative’ or ‘normative’. This document first explains the rationale, principles of MIDS and the levels of digitization, then details the information elements to be expected at each MIDS level, including their mappings to Darwin Core (DwC) terms and Access to Biological Collection Data (ABCD) terms.


## 1.4 Examples in this document

_&lt;to be added when we have some examples in the document; otherwise delete sub-section>_


## 1.5 Definitions

**basic record** – a limited set of information about the specimen; for example, physical specimen identifier and barcode details, and details of the collection it belongs to. (Cf. catalogue record, regular record and extended record).

**catalogue record** – the association between an identifier of a physical specimen and its initial digital representation, allowing for subsequent unambiguous attachment of all other information. (Cf. basic record, regular record and extended record).

**data (also known as content data)** – data relating directly to describing physical specimens, such as images of those specimens, information from specimen labels (scientific name, location where collected, date collected, collector name, etc.), links to third-party semantic resources, or measurements and other analyses of specimens.

**digital specimen** – a digital representation on the Internet (digital twin) corresponding to a physical specimen in a natural science collection.

**digitization** – the process of converting analog information about physical specimens (e.g. in natural science collections) to digital form, which therefore includes electronic text, images and other representations; and making that publicly available.

**extended record** – a comprehensive set of elements describing the specimen; for example: all label data, annotations and determination history. (Cf. catalogue record, basic record and regular record).

**levels of digitization** – a simple categorisation of the type and depth of digitization achieved by heterogeneous approaches to digitization.

**natural science collection** – a collection of natural science objects, such as preserved plants and animals, fossils, rocks and minerals, gems, etc. curated and maintained by an institution such as a museum or a university.

**persistent identifier (PID)** – a persistent identifier is a string (functioning as a symbol) that uniquely identifies a thing. The identifier can be persistently resolved to digitally actionable meaningful information about the identified thing.

**referent **– in the context of two-part information elements that name things, the referent is an identifier of an actual person, organisation, place or other thing signified by a name string, such as a collector name, museum name, place name, etc. 


    Note:	Examples of referents include: i) a person identification to disambiguate between persons sharing the same name, where an ORCID iD ([https://orcid.org/](https://orcid.org/)) can be used to disambiguate living persons while a Wikidata item ([https://www.wikidata.org/wiki/Help:Items](https://www.wikidata.org/wiki/Help:Items)) can be used to disambiguate persons unable to obtain an ORCID iD (typically, deceased collectors’ names); ii) a research organisation or collection-holding institution can be referred to by its GRID ([https://www.grid.ac/](https://www.grid.ac/)) or ROR ([https://ror.org/](https://ror.org/)) identifier.; iii) place names can be uniquey identified using GeoNames entities ([https://www.geonames.org/](https://www.geonames.org/)); and iv) in the case of a scientific name a scientific name identifier can be used to unambiguously establish a reference to the correct nomenclatural details.

**regular record** – a set of information describing the specimen; for example, physical specimen identifier, barcode details, taxon name, collection date and place, collector, etc. (Cf. catalogue record, basic record and extended record).


## 1.6 Namespaces used in this document

_&lt;to be completed when it becomes relevant; otherwise delete sub-section>_


## 1.7 Acknowledgements

This minimum information specification is the result of work carried out jointly with contributions from multiple funded projects that include:



*   CETAF Digitization Working Group;
*   European Union Horizon 2020-funded ICEDIG project (grant agreement no. 777483);
*   European Union Horizon 2020-funded SYNTHESYS+ project (grant agreement no. 823827);
*   European Union Horizon 2020-funded DiSSCo Prepare project (grant agreement no. 871043);
*   European Union COST Action CA17106 MOBILISE; and,
*   US National Science Foundation (NSF) Advancing Digitization of Biodiversity Collections Program DBI-1547229 (2016-2021), iDigBio.


# 2 Background (informative)


## 2.1 Processes of digitization (informative)

More than 3 billion physical objects cared for, organised and catalogued in thousands of natural science collections around the world represent an important data resource in botany, zoology, geology and other disciplines for research addressing scientific and societal questions. In common with most other contemporary scientific endeavours, once scientists working with such objects find themselves able to access data resources electronically without leaving their desks, they quickly find that they want to access further resources that are sometimes not so advanced in terms of ‘digital transformation’ [Meyer 2015]. An important component of digital transformation in natural sciences is the process of making data about collections and the physical objects in those collections digitally available, findable, and accessible by acquiring data from the physical objects themselves (i.e., by digitization), through curation and further processing of that data, to open data publication and use.

Digitization can lead to digital data for collections as a whole (i.e., an overview), for sub-parts of collections (inventories of trays of insects, boxes of herbarium sheets, for example) and for individual specimens. The first two categories contribute towards providing coverage and access information about the holdings of a collection-holding institution, in terms of scope and extent and are the subject of a companion specification for minimum information about a digital collection [MICS _&lt;date>_]. Digitization of specimens, which is the focus of the present specification provides explicit and precise data about each object curated in a collection. Capturing and presenting such data in standard formats is essential so that it can be easily understood, compared, analysed and communicated. Similarly, ensuring that enough data are captured, curated and published is essential so that it is useful for the widest possible range of purposes. Finally, ensuring that such data are consistently indexed and identified, such that they can be found, accessed and used is critical. This is the rationale for minimum information specifications such as the present one.


## 2.2 Stages of digitization (informative)

At the level of specimens, digitization can be characterised generally as consisting of several activities, with data created as a result of each activity:



*   Attaching an identifier to a physical specimen and creating a digital catalogue record, perhaps with its own digital identifier. This can include attaching collection-level data (from cabinets, boxes, folders, trays, etc.) to a group of specimens;
*   Specimen data capture, which can include:
    *   Making one or more images of the specimen and/or its labels; and,
    *   Extracting, processing and encoding information from those labels and images into a digital record;
*   Enriching the digital record with supplementary information that can include determinations, annotations, and/or information from a wide variety of third-party sources (references to published literature, genetic sequences, etc.).

These stages are often implemented as workflows, which can vary in their details from one institution or project to another. Nevertheless, the heterogeneity of approaches and the variations are understood [Nelson et al. 2015]. These and other differences of approach are accommodated by MIDS.


## 2.3 Harmonising the approach (informative)

Multiple digitization initiatives around the world capture digital data about specimens. An important concern in digitization is how much detail to digitize from each physical specimen. While a photographic image can often be made quickly, transcribing and interpreting all the details from labels, enriching the data with external information, and making specific measurements of the specimen take more time and resources. Often, digitization projects have been conceived to support specific scientific needs leading to variable outcomes in terms of what data is captured and how it is presented. The idea of ‘Minimum Information about a Digital Specimen’ (MIDS) has been conceived to structure this complexity.

Mobilising, unifying and delivering natural science (bio- and geo-diversity) information at the scale, form and precision required by the scientific communities can be accomplished in part by harmonising policy into guidelines about practical levels of digitization to apply and also in part by harmonising the information to be expected from each level of digitization. The present specification addresses the latter.

Harmonisation of information provides clarity about the minimum information that collection-holding institutions should be publishing in the future to make collections and digital specimens useful for multiple purposes of research, teaching and learning, etc. Similarly, by harmonising a framework that clarifies what is meant by different levels of digitization it becomes easier to consistently measure the extent of digitization achieved over time (e.g., via a collection digitization dashboard) and to set priorities for the remaining work.

The notions of extended specimens [Webster 2017] and Next Generation Collections [Schindel 2018], together with work of initiatives such as iDigBio, DiSSCo, NRCA Digital, NSII, the Biodiversity Collections Network (BCoN) and the One World Collection project further drive the need for data harmonisation. Collections-based science is global in nature and increasingly digital. In this context, barriers to interoperability and re-use must be lowered and eventually removed and global solutions are highly desirable.

The Minimum Information about a Digital Specimen (MIDS) specification, and its companion specification for information about collections – the Minimum Information about a Digital Collection (MICS) specification – aims to address these problems. Adoption and use of MIDS (and MICS) contributes to making natural sciences specimen data more compliant with the guiding principles of FAIR (‘Findable, Accessible, Interoperable, Reusable’) [Wilkinson 2016, Mons 2017].


## 2.4 Accommodating variability in details of the process (informative)

Heterogeneous approaches to digitization are accommodated in MIDS via a simple categorisation based on the form and depth of digitization achieved. 

MIDS is divided into several levels that represent a progression through the stages of digitization. Not all digitization programmes can publish all the information right from the beginning, and it is useful when collections owners publish lesser quantities at the earliest stages. Indeed, it is likely that many digitization programmes cannot or do not publish all the information at all. Only through subsequent processes of research, annotation and interpretation, and extension can specimen information become increasingly enriched and more (but never) complete. Such processes ebb and flow with the tide of scientific enquiry, contributing to and building up an ever-richer corpus of information associated with digitised artefacts. Since we can never know all there is to know about a specimen, the processes never finish and thus there can be no notion of maximum or complete information. The highest ‘gold standard’ MIDS level is open-ended to account for this.

In support of the generalised digitization workflow, MIDS defines the information elements expected at each level of digitization and strongly encourages that data resulting from digitization should be made openly available online on the Internet. Thus, in the context of MIDS, “digitized” means “online representations that are publicly available i.e., findable and accessible”. Note here that ‘accessible’ means to the extent that access is not restricted based on objective criteria defined by national security, legislation or other regulatory compliance, sensitivity of collection information, and third-party rights (such as personal privacy).

MIDS is a 'minimum specification'. This means that at any specific MIDS level a defined set of expected information elements should be the minimum amount of information made digitally available following each of the major stages of digitization identified in the generalised workflow (2.2 above). Because MIDS is a minimum specification, publishing more extensive sets of information elements is not precluded and is, in fact, recommended.

Specific practices of digitization vary widely among institutions, meaning that different elements of information can become available as the result of specific detailed workflows steps, the order of which can vary from one institution to another. MIDS accommodates this and always allows the presence of information elements additional to the expected elements at any MIDS level. These can include elements listed at higher MIDS levels, as well as other elements beyond those listed; for example, institution or collection specific elements. As a general principle, institutions should publish the fullest available data about their collections and individual specimens at the earliest opportunity, expecting that such data is likely to become enriched and annotated over time.


# 3 Principles of MIDS levels of digitization (normative)


## 3.1 Authoritative data and variations in digitization

MIDS must focus on the primary, curated scientific information denoted as being authoritative in relation to the specimen. This generally includes the ‘what, when, where, and who’ of the specimen i.e., What is it? When was it collected? Where was it collected? And who by? Apart from management information such as accession numbers, barcodes and catalogue numbers, ‘what, when, where, who’ is the minimum information usually curated in natural science collections. It is also normally a principal product of digitization processes, alongside capturing photographic images of specimens. Thus, establishing this quartet of ‘what, when, where, and who’ as the standard to be achieved as the regular level of information to be expected, is completely rational. Nevertheless, digitization processes vary from one specimen category to another and between institutions. Different levels of information – some less comprehensive, some more so – become available at different points in digitization processes. Thus, MIDS offers several levels of minimum information to be expected or achieved as the output of various stages of what is quite a variable process in the way it is conducted from one institution or collection to another.


## 3.2 Other data present or known about a specimen

In contrast to the authoritative data about a specimen, a wide variety of secondary or supplementary data may also be associated with a specimen. This can include references in literature, the results of various kinds of analysis such as (bio)chemical analysis, DNA sequencing or radiocarbon dating, links to audio and video recordings, habitat information, etc. Such data can be held with the specimen or its catalogue record, or it can be held in other institutes and databases beyond the institution holding the physical specimen. It is data that can become associated with a specimen. 

Supplementary data can either be directly related to the physical specimen, as in the case of a database record of a DNA sequence taken from a tissue sample cut from the specimen; or such data can be related only indirectly. An audio recording of the birdsong of a species that the specimen represents is an example of the latter i.e., the recording is not of that specific individual but of another in the same taxon. Indirect relations are characterised as conceptual relations rather than direct or actual relations.

MIDS optionally allows for the minimum information about a specimen to be extended by making provision to capture and publish related data.


## 3.3 Prior to digitization

In different cases, and to support processes in collection-holding institutions including accession processes and ‘digital by default’ processes, the need to create a digital record of a specimen can arise at a very early stage in the life cycle of an acquired specimen, even before digitization processes have been initiated.

In some instances, a photographic image can also be made or be already available at such a moment. Or data related to other actions, such as DNA or chemical analysis and publication can become available. Actions like taking a photograph or carrying out an analysis can take place before accession to a collection and digitization. They can occur even without a physical specimen ending up as preserved material in a collection. Such actions represent the very beginning of a digitization process and can be precursive to further digitization steps later. 

When needed at such moments, a bare catalogue record may be created to associate a specimen with a catalogue entry or database record. This should normally be via the specimen’s identifier, associating a bare minimum of digital data (a catalogue number and, ideally a persistent identifier – see 3.4 below) with a physical specimen.


        Note 1:	MIDS supports early stage digital (bare) catalogue record creation by providing a pre-level of minimum information about a digital specimen, level zero (0) that is precursive to later steps.


## 3.4 Assigning persistent identifiers to digitized specimen data

As part of the minimum information required to make digital specimen data publicly available, a persistent identifier (PID) should be assigned to a specimen and its digital data as early as possible in the digitization process; even prior to digitization commencing (see 3.3 above).


        Note 2:	Persistent and global unique identification is an important step towards making digitized specimen data publicly available online so that they can be referred to unambiguously, for example in a journal article, or so that its data can be easily found, used and updated whenever necessary. With the advent of innovative services making greater use of PIDs in the future, persistently identified specimen data is expected to become more valuable over time. 


        Note 3:	By combining a generated suffix with a prefix from the Handle system i.e., &lt;prefix>/&lt;suffix> an unambiguous, persistent (long-lasting) resolvable reference to the digital specimen’s information can be created.


        Note 4:	Beyond the recommendation above, the topic of persistent identification of specimen data is outside the scope of the present document.


## 3.5 MIDS levels of minimum information

As outlined in Table 1, MIDS specifies three levels of ‘minimum information’, together with a pre-level, level zero (0). Excepting level 0, each MIDS level of minimum information is a superset of the preceding level.

**Table 1: MIDS levels of minimum information**


<table>
  <tr>
   <td><strong>MIDS level</strong>
   </td>
   <td><strong>Record extent</strong>
   </td>
   <td><strong>Purpose</strong>
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>Basic
   </td>
   <td>A basic record of specimen information.
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>Regular
   </td>
   <td>Key information fields that have been agreed over time as essential for most scientific purposes.
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>Extended
   </td>
   <td>Other data present or information known about the specimen, including links to third-party sources.
   </td>
  </tr>
  <tr>
   <td><em>0 \
(Note)</em>
   </td>
   <td><em>Bare</em>
   </td>
   <td><em>A bare or skeletal record making the association between an identifier of a physical specimen and its digital representation, allowing for unambiguous attachment of all other information.</em>
   </td>
  </tr>
  <tr>
   <td colspan="3" >
    Note:	Level 0 is equivalent to creating a simple catalogue record containing a physical specimen identifier, such as a barcode number. Level 0 often precedes fuller digitization steps that yield more detailed information. Hence, level 0 is termed a pre-level. Nevertheless, level 0 data is useful minimum information for advertising or knowing about the existence of specimens.
   </td>
  </tr>
</table>


**<span style="text-decoration:underline;">MIDS level 1</span>** is a basic level of information about a specimen. The creation of a basic digital record with a globally unique identifier enables all other information (including images and/or other media types) to be associated unambiguously with a single physical specimen. The elements of name and geographical region are often included to create a virtual representation of the physical collections, enabling similar search and browsing capabilities online as researchers and curators would have at the cabinets of physical specimens.

**<span style="text-decoration:underline;">MIDS level 2</span>** is the regular level of information expected to be known about a specimen. Regular records include the latitude/longitude data which, along with taxon name, are critical for many research applications. For botanical specimens the inclusion of collector name, number and date are a priority, given their historical use in acting as the identifier for the specimen in literature. These terms are routinely used to identify the specimen in requests to curation staff.

**<span style="text-decoration:underline;">MIDS level 3</span>** is an extended or rich level of information about a specimen. Extended or rich records include other data present or known about the specimen. Such records will need to be updated as additional labels and other information are added to the specimen over time. At level 3 there is no notion of completeness or of a full or complete record because new information is always valuable and can be added to an existing record at any time.

**<span style="text-decoration:underline;">MIDS level 0</span>** (usually being established prior to any formal digitization and hence considered a pre-level) is a bare level of information that exists to make an association between a physical specimen with its identifier (barcode, for example) and an entry in a catalogue or database. One early action in a digitization process is the creation of a database record that acknowledges or coincides with the existence or accession of a physical specimen into a collection, but not necessarily with any other information digitized at that stage. Note, however that image(s) can be generated and referenced at this early stage.


## 3.6 Information elements expected and expansion beyond the minimum

At each level, MIDS defines the information elements that must be present. This is specified in section 4 below

In addition to the information elements expected to be present as a minimum, MIDS must always allow the presence of other information elements beyond the minimum, including institutional and collection specific elements.


        Note 5:	It is not precluded and is encouraged that institutions publish information beyond the minimum. However, information does not qualify as meeting a specific MIDS level unless all the information elements expected at that level are available with actual values.


# 4 Information content and element mappings for each MIDS level (normative)


            _Editor’s note:	At present (July 2020) the MIDS information elements in Table 2 – Table 5 are given as information element descriptions, and not as term names. The expectation is that term names will be coined based on the forthcoming TDWG work to better integrate and harmonise across DwC, ABCD, BCO and Taxonomic Names and Concepts as proposed here at Biodiversity_Next 2019: [https://doi.org/10.3897/biss.3.37491](https://doi.org/10.3897/biss.3.37491). MIDS is, in effect, likely to be a documented application profile across these standards._

Sections 4.1 - 4.4 list in tables the information elements expected to be present at MIDS levels 1, 2, 3 and 0 respectively. Section 4.5 gives additional requirements for handling of unknown or incomplete data that must be applied in conjunction with the relevant information elements.


## 4.1 Information elements expected at MIDS level 1

The information elements expected to be present in digital specimen data published at MIDS level 1 are listed in Table 2.

**Table 2: MIDS Level 1: Expected elements, mappings and recommendations for a basic record**


<table>
  <tr>
   <td><strong>MIDS information elements</strong>
   </td>
   <td><strong>DwC term \
 (latest, 2014-11-08)</strong>
   </td>
   <td><strong>ABCD term name \
 (3.0)</strong>
   </td>
   <td><strong>Recommendations</strong>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>CreatedOn \
(date/time of record creation)
</li>
</ol>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td>hasDateCreated
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>ModifiedOn \
(date/time of subsequent modification, if any)
</li>
</ol>
   </td>
   <td>modified
   </td>
   <td>hasDateModified
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>RecordCreator \
 i) Name \
 ii) Referent
</li>
</ol>
   </td>
   <td><em> \
No equivalent \
No equivalent</em>
   </td>
   <td> \
hasCreators \
<em>No equivalent</em>
   </td>
   <td> \
Person’s name. \
ORCID ID if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>MIDSLevel
</li>
</ol>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td>Integer, value = 1.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PhysicalSpecimenId \
(physical specimen identifier, barcode, catalog number, etc.
</li>
</ol>
   </td>
   <td>catalogNumber
   </td>
   <td>physicalObjectIDId
   </td>
   <td>Cardinality 0..n.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Institution \
 i) Code \
 ii) Referent
</li>
</ol>
   </td>
   <td> \
institutionCode \
<em>No equivalent</em>
   </td>
   <td> \
sourceInstitutionID \
<em>No equivalent</em>
   </td>
   <td> \
from GrSciColl. \
GRID/ROR; else ‘unknown’. 
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>MaterialType
</li>
</ol>
   </td>
   <td>preparations
   </td>
   <td>preparationsText
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>ScientificName \
 i) Name appropriate to the \
    specimen \
ii) Referent
</li>
</ol>
   </td>
   <td> \
scientificName \
 \
scientificNameID
   </td>
   <td> \
FullScientificName \
 \
<em>No equivalent</em>
   </td>
   <td> \
 \
 \
A name identifier, uniquely identifying the name; else ‘unknown’.
   </td>
  </tr>
</table>


An image and/or other multimedia may be present (see 5 below).


## 4.2 Information elements expected at MIDS level 2

The information elements expected to be present in digital specimen data published at MIDS level 2 are listed in Table 3.

**Table 3: MIDS Level 2: Expected elements, mappings and recommendations for a regular record**


<table>
  <tr>
   <td><strong>MIDS information elements</strong>
   </td>
   <td colspan="2" ><strong>DwC term \
 (latest, 2014-11-08)</strong>
   </td>
   <td><strong>ABCD term name \
 (3.0)</strong>
   </td>
   <td><strong>Recommendations</strong>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>CreatedOn \
(date/time of record creation)
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td>hasDateCreated
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>ModifiedOn \
(date/time of subsequent modification, if any)
</li>
</ol>
   </td>
   <td colspan="2" >modified
   </td>
   <td>hasDateModified
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>RecordCreator \
 i) Name \
 ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" ><em> \
No equivalent \
No equivalent</em>
   </td>
   <td> \
hasCreators \
<em>No equivalent</em>
   </td>
   <td> \
Person’s name. \
ORCID ID if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>MIDSLevel
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td>Integer, value = 2.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PhysicalSpecimenId \
(physical specimen identifier, barcode, catalog number, etc.
</li>
</ol>
   </td>
   <td colspan="2" >catalogNumber
   </td>
   <td>physicalObjectIDId
   </td>
   <td>Cardinality 0..n.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Institution \
 i) Code \
 ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
institutionCode \
<em>No equivalent</em>
   </td>
   <td> \
sourceInstitutionID \
<em>No equivalent</em>
   </td>
   <td> \
from GrSciColl. \
GRID/ROR; else ‘unknown’. 
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>MaterialType
</li>
</ol>
   </td>
   <td colspan="2" >preparations
   </td>
   <td>preparationsText
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>ScientificName \
 i) Name appropriate to the \
    specimen \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
scientificName \
 \
scientificNameID
   </td>
   <td> \
FullScientificName \
 \
<em>No equivalent</em>
   </td>
   <td> \
 \
 \
A name identifier, uniquely identifying the name; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Continent
</li>
</ol>
   </td>
   <td colspan="2" >continent
   </td>
   <td>NamedArea/ \
 areaClass
   </td>
   <td>Table Note 1.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Country
</li>
</ol>
   </td>
   <td colspan="2" >country
   </td>
   <td>Country
   </td>
   <td>Use [ISO 3166].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>State/province
</li>
</ol>
   </td>
   <td colspan="2" >stateProvince
   </td>
   <td>NamedArea/ \
 areaClass
   </td>
   <td>Use [ISO 3166].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>County \
i) Name \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
county
   </td>
   <td> \
NamedArea/ \
 areaClass
   </td>
   <td> \
Use [ISO 3166]. \
GeoNames identifier if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Locality \
i) Name \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
locality
   </td>
   <td> \
NamedArea/ \
 areaClass
   </td>
   <td> \
Locality name. \
GeoNames identifier if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Latitude/longitude
</li>
</ol>
   </td>
   <td colspan="2" >decimalLatitude, decimalLongitude
   </td>
   <td>latitudeDecimal, \
longitudeDecimal
   </td>
   <td>If known; else “unknown”. Include georeference datum, source and uncertainty if known; else “unknown”.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Altitude/depth
</li>
</ol>
   </td>
   <td colspan="2" >verbatimElevation or \
verbatimDepth
   </td>
   <td>hasAltitude or \
hasDepth
   </td>
   <td>If known; else “unknown”.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collector name \
i) Name \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
recordedBy
   </td>
   <td> \
Gathering/ \
 hasGatheringAgent
   </td>
   <td> \
Person’s name. \
?? identifier if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collector number
</li>
</ol>
   </td>
   <td colspan="2" >recordNumber
   </td>
   <td><em>No equivalent</em>
   </td>
   <td> “s.n.” or equivalent if not present
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collection date
</li>
</ol>
   </td>
   <td colspan="2" >eventDate
   </td>
   <td>Gathering/hasDate
   </td>
   <td>“s.d.” or equivalent if not present
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collection code/name
</li>
</ol>
   </td>
   <td colspan="2" >collectionCode
   </td>
   <td>sourceID
   </td>
   <td>What source/standard?
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Type status
</li>
</ol>
   </td>
   <td colspan="2" >typeStatus
   </td>
   <td>nomenclaturalTypeText
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Geographical region
</li>
</ol>
   </td>
   <td colspan="2" >higherGeography
   </td>
   <td>NamedArea
   </td>
   <td>Table Note 1.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Deposited/accession date
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td>Accession/hasDate
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Name identifier
</li>
</ol>
   </td>
   <td colspan="2" >identificationID
   </td>
   <td>Identification/ \
 hasIdentifiedTaxon
   </td>
   <td>Uniquely identifying name in 8. ScientificName 
   </td>
  </tr>
  <tr>
   <td colspan="5" >Note 1: Geographical region should be identified in one of three major categories: terrestrial (WGSRPD level 1 areas, [Brummitt 2001]), marine (IHO World Seas, [FMI 2018]) or extra-terrestrial. The geographical region value must be specified in two parts i.e., Terrestrial:&lt;regionname below> or Marine:&lt;seaname below> or Extra-terrestrial:Extra-terrestrial. World/NA should be used when a more specific regional classification is not known.
   </td>
  </tr>
  <tr>
   <td colspan="2" >
    Terrestrial:
<p>

    Europe, Africa, Asia Temperate, Asia Tropical, Australasia, Pacific, North America, South America, Antarctic, World/NA
   </td>
   <td colspan="3" >Marine:
<p>

    North Pacific, South Pacific, North Atlantic, South Atlantic, Indian, Southern, Arctic Marine, World/NA
   </td>
  </tr>
</table>


An image and/or other multimedia may be present (see 5 below).


## 4.3 Information elements expected at MIDS level 3

The information elements expected to be present in digital specimen data published at MIDS level 3 are listed in Table 4.

**Table 4: MIDS Level 3: Expected elements, mappings and recommendations for an extended record**


<table>
  <tr>
   <td><strong>MIDS information elements</strong>
   </td>
   <td colspan="2" ><strong>DwC term \
 (latest, 2014-11-08)</strong>
   </td>
   <td><strong>ABCD term name \
 (3.0)</strong>
   </td>
   <td><strong>Recommendations</strong>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>CreatedOn \
(date/time of record creation)
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td>hasDateCreated
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>ModifiedOn \
(date/time of subsequent modification, if any)
</li>
</ol>
   </td>
   <td colspan="2" >modified
   </td>
   <td>hasDateModified
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>RecordCreator \
 i) Name \
 ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" ><em> \
No equivalent \
No equivalent</em>
   </td>
   <td> \
Creators \
<em>No equivalent</em>
   </td>
   <td> \
Person’s name. \
ORCID ID if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>MIDSLevel
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td>Integer, value = 2.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PhysicalSpecimenId \
(physical specimen identifier, barcode, catalog number, etc.
</li>
</ol>
   </td>
   <td colspan="2" >catalogNumber
   </td>
   <td>Id
   </td>
   <td>Cardinality 0..n.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Institution \
 i) Code \
 ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
institutionCode \
<em>No equivalent</em>
   </td>
   <td> \
sourceInstitutionID \
<em>No equivalent</em>
   </td>
   <td> \
from GrSciColl. \
GRID/ROR; else ‘unknown’. 
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>MaterialType
</li>
</ol>
   </td>
   <td colspan="2" >preparations
   </td>
   <td>preparationsText
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>ScientificName \
 i) Name appropriate to the \
    specimen \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
scientificName \
 \
scientificNameID
   </td>
   <td> \
FullScientificName \
 \
<em>No equivalent</em>
   </td>
   <td> \
 \
 \
A name identifier, uniquely identifying the name; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Continent
</li>
</ol>
   </td>
   <td colspan="2" >continent
   </td>
   <td>NamedArea/ \
 areaClass
   </td>
   <td>Table Note 2.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Country
</li>
</ol>
   </td>
   <td colspan="2" >country
   </td>
   <td>Country
   </td>
   <td>Use [ISO 3166].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>State/province
</li>
</ol>
   </td>
   <td colspan="2" >stateProvince
   </td>
   <td>NamedArea/ \
 areaClass
   </td>
   <td>Use [ISO 3166].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>County \
i) Name \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
county
   </td>
   <td> \
NamedArea/ \
 areaClass
   </td>
   <td> \
Use [ISO 3166]. \
GeoNames identifier if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Locality \
i) Name \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
locality
   </td>
   <td> \
NamedArea/ \
 areaClass
   </td>
   <td> \
Locality name. \
GeoNames identifier if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Latitude/longitude
</li>
</ol>
   </td>
   <td colspan="2" >decimalLatitude, decimalLongitude
   </td>
   <td>latitudeDecimal, \
longitudeDecimal
   </td>
   <td>If known; else “unknown”. Include georeference datum, source and uncertainty if known; else “unknown”.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Altitude/depth
</li>
</ol>
   </td>
   <td colspan="2" >verbatimElevation or \
verbatimDepth
   </td>
   <td>hasAltitude or \
hasDepth
   </td>
   <td>If known; else “unknown”.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collector name \
i) Name \
ii) Referent
</li>
</ol>
   </td>
   <td colspan="2" > \
recordedBy
   </td>
   <td> \
Gathering/ \
 hasGatheringAgent
   </td>
   <td> \
Person’s name. \
?? identifier if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collector number
</li>
</ol>
   </td>
   <td colspan="2" >recordNumber
   </td>
   <td><em>No equivalent</em>
   </td>
   <td> “s.n.” or equivalent if not present
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collection date
</li>
</ol>
   </td>
   <td colspan="2" >eventDate
   </td>
   <td>Gathering/hasDate
   </td>
   <td>“s.d.” or equivalent if not present
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Collection code/name
</li>
</ol>
   </td>
   <td colspan="2" >collectionCode
   </td>
   <td>sourceID
   </td>
   <td>What source/standard?
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Type status
</li>
</ol>
   </td>
   <td colspan="2" >typeStatus
   </td>
   <td>nomenclaturalTypeText
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Geographical region
</li>
</ol>
   </td>
   <td colspan="2" >higherGeography
   </td>
   <td>NamedArea
   </td>
   <td>Table Note 2.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Deposited/accession date
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td>Accession/hasDate
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Name identifier
</li>
</ol>
   </td>
   <td colspan="2" >identificationID
   </td>
   <td>Identification/ \
 hasIdentifiedTaxon
   </td>
   <td>Uniquely identifying name in 8. ScientificName 
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Determination(s)	
</li>
</ol>
   </td>
   <td colspan="2" >
   </td>
   <td>identifiedBy
   </td>
   <td>All determinations (with taxon name identifier) including the determiner (with the person name identifier)
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Remaining transcription from original collection label
</li>
</ol>
   </td>
   <td colspan="2" >
   </td>
   <td>
   </td>
   <td>All information from the original collection label not alreadyto be transcribed
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Quality assertions
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td><em>Element for further study.</em>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PID links to image(s)
</li>
</ol>
   </td>
   <td colspan="2" ><em>No equivalent</em>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td><em>Element for further study.</em>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PID links to other data present or information known about the specimen
</li>
</ol>
   </td>
   <td colspan="2" >Table Note 2.
   </td>
   <td>
   </td>
   <td><em>Element for further study.</em>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PID links to annotations
</li>
</ol>
   </td>
   <td colspan="2" >
   </td>
   <td>
   </td>
   <td><em>Element for further study.</em>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PID links to interpretations
</li>
</ol>
   </td>
   <td colspan="2" >
   </td>
   <td>
   </td>
   <td><em>Element for further study.</em>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PID links to provenance
</li>
</ol>
   </td>
   <td colspan="2" >
   </td>
   <td>
   </td>
   <td><em>Element for further study.</em>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Institutional persistent identifier (CETAF Stable Identifier/URI)
</li>
</ol>
   </td>
   <td colspan="2" >
   </td>
   <td>
   </td>
   <td><em>Element for further study.</em>
   </td>
  </tr>
  <tr>
   <td colspan="5" >Note 1: Geographical region should be identified in one of three major categories: terrestrial (WGSRPD level 1 areas, [Brummitt 2001]), marine (IHO World Seas, [FMI 2018]) or extra-terrestrial. The geographical region value must be specified in two parts i.e., Terrestrial:&lt;regionname below> or Marine:&lt;seaname below> or Extra-terrestrial:Extra-terrestrial. World/NA should be used when a more specific regional classification is not known.
   </td>
  </tr>
  <tr>
   <td colspan="2" >
    Terrestrial:
<p>

    Europe, Africa, Asia Temperate, Asia Tropical, Australasia, Pacific, North America, South America, Antarctic, World/NA
   </td>
   <td colspan="3" >Marine:
<p>

    North Pacific, South Pacific, North Atlantic, South Atlantic, Indian, Southern, Arctic Marine, World/NA
   </td>
  </tr>
  <tr>
   <td colspan="5" >Note 2: For example: associatedReferences, associatedSequences, associatedOccurrences, associatedOrganisms, geologicalContextID, identificationID, taxonID, scientificNameID, dynamicProperties, etc.
   </td>
  </tr>
</table>


An image and/or other multimedia may be present (see 5 below).

For discussion: At MIDS level 3, Extended, we would expect interpreted, added data that has not been directly extracted from the physical object but rather from already available digital data. Examples are links to publications, georeferenced data etc. Question is how to quantify this level, as it can have many/any enrichments.


## 4.4 Information elements expected at MIDS level 0

The information elements expected to be present in digital specimen data published at MIDS level 0 are listed in Table 5.

**Table 5: MIDS Level 0: Expected elements, mappings and recommendations for a bare record**


<table>
  <tr>
   <td><strong>MIDS information elements</strong>
   </td>
   <td><strong>DwC term \
 (latest, 2014-11-08)</strong>
   </td>
   <td><strong>ABCD term name \
 (3.0)</strong>
   </td>
   <td><strong>Recommendations</strong>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>CreatedOn \
(date/time of record creation)
</li>
</ol>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td>hasDateCreated
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>ModifiedOn \
(date/time of subsequent modification, if any)
</li>
</ol>
   </td>
   <td>modified
   </td>
   <td>hasDateModified
   </td>
   <td>Use [ISO 8601].
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>RecordCreator \
 i) Name \
 ii) Referent 
</li>
</ol>
   </td>
   <td><em> \
No equivalent \
No equivalent</em>
   </td>
   <td> \
Creators \
<em>No equivalent</em>
   </td>
   <td> \
Person’s name. \
ORCID ID] if known; else ‘unknown’.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>MIDSLevel
</li>
</ol>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td><em>No equivalent</em>
   </td>
   <td>Integer, value = 0.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>PhysicalSpecimenId \
(physical specimen identifier, barcode, catalog number, etc.
</li>
</ol>
   </td>
   <td>catalogNumber
   </td>
   <td>Id
   </td>
   <td>Cardinality: 0..n.
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li>Institution \
 i) Code \
 ii) Referent
</li>
</ol>
   </td>
   <td> \
institutionCode \
<em>No equivalent</em>
   </td>
   <td> \
sourceInstitutionID \
<em>No equivalent</em>
   </td>
   <td> \
from GrSciColl. \
GRID/ROR; else ‘unknown’. 
   </td>
  </tr>
</table>


An image and/or other multimedia may be present (see 5 below).

~~For discussion: There’s a suggestion that at this level, some information relating to the position of the specimen in a collection might be available and should be presented. This might be, for example a higher classification rank related to the specimen’s placement in a collection. Does this count as minimum information?~~


## 4.5 Handling of unknown and incomplete data

Best practice dictates that wherever possible data should not be published with empty field values as this is misleading for both human users and machines. There are many reasons why data can be missing, unknown, incomplete or explicitly withheld [Groom 2019] and various tactics have been used in the past to deal with such situations. However, with the increasing use of machines to interpret and act upon data, variable past practices should be deprecated, and new, more consistent practices promoted. In the interest of presenting more meaningful corpora of minimum specimen information in the future, the present specification (4.5.1 - 4.5.3 below) recommends harmonising an approach for presenting minimum information fields where the content of those fields can be unknown or incomplete for a variety of reasons.


### 4.5.1 Unknown datetime in CreatedON/ModifiedON information elements

If the creation and/or modification date/time of a specimen data record is not known, the standard form for unspecified date/time, as specified in ISO 8601-2:2019 should be used for the createdON and/or modifiedON information element(s) i.e., “X*” or “XXXX-XX-XX”.


### 4.5.2 Geographical data information elements

To achieve MIDS level 2, each geographical information element listed in Table 3 (i.e., Continent, Country, State/province, County, Locality, Latitude/longitude, Altitude/depth, Geographical Region) must be provided.

If such information is not present on the specimen label, but can be inferred/interpreted from other information present or from other sources, it should be provided. If such information is not present and cannot be inferred it should be recorded as “unknown:missing” (4.5.3 below).

Country level information has particular importance and this (or at least one other more localised named area) should always be provided.

_Editor’s note: Do we really need to state the above requirement?_

_Editor’s note: Need marine/ET equivalents too._


### 4.5.3 Unknown values for other information elements

Table 6 lists the terms that should be used in lieu of any of the information elements listed in Table 2 – Table 4 above being left empty.

**Table 6: Terms for missing data values in lieu of empty information elements**

Based on [Groom 2019], Table 1. [CC BY](https://creativecommons.org/licenses/by/4.0/).


<table>
  <tr>
   <td><strong>Missing data term</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
   <td><strong>Example</strong>
   </td>
  </tr>
  <tr>
   <td>unknown \
(Note 1)
   </td>
   <td>The information is not digitally available.
   </td>
   <td>Empty value in a digital record of unknown provenance.
   </td>
  </tr>
  <tr>
   <td>unknown:undigitized \
(Note 1, Note 2)
   </td>
   <td>The information is not digitally available. No attempt has been made to digitize it.
   </td>
   <td>Empty value in a skeletal record to which data still need to be added from the label.
   </td>
  </tr>
  <tr>
   <td>unknown:missing \
(Note 1, Note 2)
   </td>
   <td>The information is not digitally available. It appeared to be absent during digitization.
   </td>
   <td>A value of S.D. (<em>sine dato</em>) used by transcription platforms to indicate the absence of a date value.
   </td>
  </tr>
  <tr>
   <td>unknown:indecipherable \
(Note 1, Note 2)
   </td>
   <td>The information is not digitally available. It appeared to be present during digitization but failed to be captured.
   </td>
   <td>An indication made by a transcriber that they failed to transcribe the information.
   </td>
  </tr>
  <tr>
   <td>known:withheld \
(Note 3)
   </td>
   <td>The information is digitally available, but it has been withheld by the provider.
   </td>
   <td>A georeferenced record for which coordinate data are available but withheld for conservation reasons.
   </td>
  </tr>
  <tr>
   <td>known:undigitized
   </td>
   <td>The information is known but has not been digitized (i.e., it is not digitally available).
   </td>
   <td>Label information that has not been transcribed because the digitization request/purpose does not require it.
   </td>
  </tr>
  <tr>
   <td>Not applicable
   </td>
   <td>The information element is not applicable
   </td>
   <td>One or more of the information elements 23 onwards in Table 4 may not be applicable. Some information elements are not applicable for some kinds of collection.
   </td>
  </tr>
  <tr>
   <td colspan="3" >
    Note 1:	The generic unknown indicates that the information is indeed not available.
<p>

    Note 2:	The additives undigitized, missing and indecipherable allow elaboration as to why the data are unavailable, if this reason is known.
<p>

    Note 3:	known:withheld indicates that the data are digitally available in a more primary source and could potentially be retrieved after contacting the data provider.
   </td>
  </tr>
</table>



# 5 Images and other media types (normative)

Many but not all digitization projects and programmes produce images of specimens and their accompanying label(s). It is helpful to users and machines, when searching for available digital specimens to know if images are available. Thus, a MIDS level may be supplemented with one or both the designators specified in Table 7. 

As part of the minimum information about a specimen, digital specimens should (if possible) include at least one image of the complete specimen and its accompanying label(s). If images are present, the MIDS level of the digital specimen must be supplemented with the indicator ‘i’ indicating the availability of image(s).

Digital specimens may include multiple images of different types and/or other types of media. If other media type(s) are present, the MIDS level of the digital specimen shall be supplemented with the indicator ‘m’ to indicate the availability of other media type(s).

**Table 7: Media elements of MIDS record types**


<table>
  <tr>
   <td><strong>MIDS level</strong>
   </td>
   <td><strong>Object image type</strong>
   </td>
   <td><strong>Recommendation</strong>
   </td>
  </tr>
  <tr>
   <td>i
   </td>
   <td>Object image with label
   </td>
   <td>Image should include the whole specimen where possible. Original label(s) should be included either in the same image or as separate images.
   </td>
  </tr>
  <tr>
   <td>m
   </td>
   <td>Other multimedia present
   </td>
   <td>No specific recommendation.
   </td>
  </tr>
</table>


Specimens can require more than one image to properly display all features of interest. Thus, multiple images can be present for a specimen. However, characterising the number and nature of image and other multimedia types available as outputs of digitization processes is outside the scope of the present specification.


# 6 Guidelines for machine-actionability (normative)

To do: &lt;insert text. This is the publishing/sharing aspect that is often treated separate from and after digitization. Publicly available means not only to humans but also for machines to find/access as well. FAIR statement of how MIDS supports each of the 15 principles.>


# 7 Recommendations for collection-holding institutions

MIDS is a minimum standard. As a general principle, institutions should aim to publish the fullest available data about their collections and individual specimens at the earliest opportunity. This means as soon as practically possible after digitization, verification and curation activities have been carried out, expecting that such data can and will be enriched and annotated over time by exposure to a broad expert audience.

The minimum amount of information to be made available (published) must be the expected information elements at any chosen level of digitization.

As best practice, level 2 Regular should be the minimum standard to aim for. However, publishing information in accordance with levels 1 Basic and/or 0 Catalogue and enriching it over time is acceptable.

The information elements expected by MIDS at any level of digitization are the minimum amount of information to be published. As the gold standard, collection-holding institutions are encouraged to publish beyond the minimum where possible, and to aspire to Level 3 Extended.

To do>> We probably want to say something here about how to apply MIDS retrospectively to records already digitized.


# 8 Guarding against publication of junk data

Concerns about publishing junk data are not solved by MIDS. Collection-holding institutions should operate adequate quality controls during digitization processes to ensure that published data are valid data, to the best of knowledge. Attention to prevention of digitization errors, simple (automated) checks and basic rules, such as avoiding unfilled information fields (i.e., use specific ‘unknown’ or ‘not specified’ values instead of leaving fields blank) each contribute to ensuring valid data.


# 9 Conformance (normative)


## 9.1 Principle means of conformance

The principle means of conformance with the present specification must be through implementation of its requirements in workflows and processes of specimen digitization and data management.


        Note 7:	Tools for automated verification of MIDS levels may become available in the future. 


## 9.2 Implementation Conformance Statement (ICS)

The Implementation Conformance Statement (ICS) proforma in Table 8 – Table 11 is a checklist collection-holding institutions and others can use to check and self-declare their conformance with the requirements of the present specification.

In the support column for each item, an assessor must answer the status questions with “yes” or “no” by ticking/unticking the checkboxes. Status values have the following meanings:


        m	mandatory to support the item/provide the information.


        o	optional to support the item/provide the information.


        m.N	mandatory to support at least one of the items/provide the information in the group N.


        o.N	optional to support one or more of the items/provide the information in the group N.


        c.N	conditional on item N. Answering the items in the table is conditional on the answer for item N.


    _Editor’s note: On completion of proforma rows, numbering and cross-referencing to be checked/completed._

**Table 8: ICS proforma for MIDS conformance (general)**


<table>
  <tr>
   <td><strong>Item</strong>
   </td>
   <td><strong>Requirement</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Status</strong>
   </td>
   <td><strong>Support</strong>
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>Focus on the primary, curated scientific information denoted as being authoritative for the specimen
   </td>
   <td>§3.1
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>Publish specimen data at MIDS level 0
   </td>
   <td>§3.5
   </td>
   <td>m.1
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>Publish specimen data at MIDS level 1
   </td>
   <td>§3.5
   </td>
   <td>m.1
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>Publish specimen data at MIDS level 2
   </td>
   <td>§3.5
   </td>
   <td>m.1
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td>Publish specimen data at MIDS level 3
   </td>
   <td>§3.5
   </td>
   <td>m.1
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td>Unknown / unspecified datetime form supported i.e., “X*” or “XXXX-XX-XX”
   </td>
   <td>§4.5.1
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td>
   </td>
   <td>§4.5.2
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>



    m.1: It is mandatory to support at least one of these items 2 – 5.

**Table 9: ICS proforma for MIDS level 0 conformance**


<table>
  <tr>
   <td colspan="3" >c.2: yes, no, n/a* (select according to answer in Table 8). If yes, complete this table.
   </td>
   <td colspan="2" >Choose an item.
   </td>
  </tr>
  <tr>
   <td><strong>Item</strong>
   </td>
   <td><strong>Requirement</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Status</strong>
   </td>
   <td><strong>Support</strong>
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td>CreatedOn
   </td>
   <td>Table 5 1.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td>ModifiedOn
   </td>
   <td>Table 5 2.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>8
   </td>
   <td>RecordCreator \
 i) Name \
 ii) Referent
   </td>
   <td>Table 5 3.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>9
   </td>
   <td>MidsLevel
   </td>
   <td>Table 5 4.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td>PhysicalSpecimenId
   </td>
   <td>Table 5 5.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>11
   </td>
   <td>Institution \
 i) Code \
 ii) Referent
   </td>
   <td>Table 5 6.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>12
   </td>
   <td>MaterialType
   </td>
   <td>Table 5 7.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13
   </td>
   <td>ScientificName
<p>
 i) Name appropriate to the specimen
<p>
ii) Referent
   </td>
   <td>Table 5 8.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>14
   </td>
   <td>Has image(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>15
   </td>
   <td>Has other media type(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>


**Table 10: ICS proforma for MIDS level 1 conformance**


<table>
  <tr>
   <td colspan="3" >c.3: yes, no, n/a* (select according to answer in Table 8). If yes, complete this table.
   </td>
   <td colspan="3" >Choose an item.
   </td>
  </tr>
  <tr>
   <td><strong>Item</strong>
   </td>
   <td><strong>Requirement</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Status</strong>
   </td>
   <td><strong>Support</strong>
   </td>
  </tr>
  <tr>
   <td>16
   </td>
   <td>CreatedOn
   </td>
   <td>Table 2 1.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>17
   </td>
   <td>ModifiedOn
   </td>
   <td>Table 2 2.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>18
   </td>
   <td>RecordCreator \
 i) Name \
 ii) Referent
   </td>
   <td>Table 2 3.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>19
   </td>
   <td>MIDSLevel
   </td>
   <td>Table 2 4.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>20
   </td>
   <td>PhysicalSpecimenId
   </td>
   <td>Table 2 5.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>21
   </td>
   <td>Institution \
 i) Code \
 ii) Referent
   </td>
   <td>Table 2 6.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>22
   </td>
   <td>MaterialType
   </td>
   <td>Table 2 7.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>23
   </td>
   <td>ScientificName
<p>
 i) Name appropriate to the specimen
<p>
ii) Referent
   </td>
   <td>Table 2 8.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>24
   </td>
   <td>Has image(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>25
   </td>
   <td>Has other media type(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>


**Table 11: ICS proforma for MIDS level 2 conformance**

_Editor’s note: Proforma to be completed._


<table>
  <tr>
   <td colspan="3" >c.4: yes, no, n/a* (select according to answer in Table 8). If yes, complete this table.
   </td>
   <td colspan="3" >Choose an item.
   </td>
  </tr>
  <tr>
   <td><strong>Item</strong>
   </td>
   <td><strong>Requirement</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Status</strong>
   </td>
   <td><strong>Support</strong>
   </td>
  </tr>
  <tr>
   <td>26
   </td>
   <td>CreatedOn
   </td>
   <td>Table 3 1.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>27
   </td>
   <td>ModifiedOn
   </td>
   <td>Table 3 2.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>28
   </td>
   <td>RecordCreator \
 i) Name \
 ii) Referent
   </td>
   <td>Table 3 3.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>29
   </td>
   <td>MIDSLevel
   </td>
   <td>Table 3 4.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>30
   </td>
   <td>PhysicalSpecimenId
   </td>
   <td>Table 3 5.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>31
   </td>
   <td>Institution \
 i) Code \
 ii) Referent
   </td>
   <td>Table 3 6.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>32
   </td>
   <td>MaterialType
   </td>
   <td>Table 3 7.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>33
   </td>
   <td>ScientificName
<p>
 i) Name appropriate to the specimen
<p>
ii) Referent
   </td>
   <td>Table 3 8.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><em>Editor’s note: Proforma to be completed.</em>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>nn
   </td>
   <td>Has image(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>nn
   </td>
   <td>Has other media type(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>


**Table 12: ICS proforma for MIDS level 3 conformance**

_Editor’s note: Proforma to be completed._


<table>
  <tr>
   <td colspan="3" >c.5: yes, no, n/a* (select according to answer in Table 8). If yes, complete this table.
   </td>
   <td colspan="3" >Choose an item.
   </td>
  </tr>
  <tr>
   <td><strong>Item</strong>
   </td>
   <td><strong>Requirement</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Status</strong>
   </td>
   <td><strong>Support</strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>CreatedOn
   </td>
   <td>Table 4 1.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>ModifiedOn
   </td>
   <td>Table 4 2.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Unknown / unspecified datetime form i.e., “X*” or “XXXX-XX-XX”
   </td>
   <td>Table 4 \
Note 1
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>RecordCreator \
 i) Name \
 ii) Referent
   </td>
   <td>Table 4 3.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>MIDSLevel
   </td>
   <td>Table 4 4.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>PhysicalSpecimenId
   </td>
   <td>Table 4 5.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Institution \
 i) Code \
 ii) Referent
   </td>
   <td>Table 4 6.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>MaterialType
   </td>
   <td>Table 4 7.
   </td>
   <td>m
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>ScientificName
<p>
 i) Name appropriate to the specimen
<p>
ii) Referent
   </td>
   <td>Table 4 8.
   </td>
   <td> \
m \
o
   </td>
   <td> \
☐ \
☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><em>Editor’s note: Proforma to be completed.</em>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Has image(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Has other media type(s)
   </td>
   <td>§5
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>


**Table 13: ICS proforma for handling of unknown or incomplete data**


<table>
  <tr>
   <td><strong>Item</strong>
   </td>
   <td><strong>Requirement</strong>
   </td>
   <td><strong>Reference</strong>
   </td>
   <td><strong>Status</strong>
   </td>
   <td><strong>Support</strong>
   </td>
  </tr>
  <tr>
   <td>13.1
   </td>
   <td>Unknown / unspecified datetime “X*” form (ISO 8601-2)
   </td>
   <td>§4.5.1
   </td>
   <td>o.2
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.2
   </td>
   <td>Unknown / unspecified datetime “XXXX-XX-XX” form (ISO 8601-2)
   </td>
   <td>§4.5.1
   </td>
   <td>o.2
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.3
   </td>
   <td>… ...
   </td>
   <td>§4.5.2
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.4
   </td>
   <td>Unknown data term “unknown”
   </td>
   <td>§4.5.3
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.5
   </td>
   <td>
    Unknown data term “unknown:undigitized”
   </td>
   <td>§4.5.3
   </td>
   <td>c13.3:o.3
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.6
   </td>
   <td>
    Unknown data term “unknown:missing”
   </td>
   <td>§4.5.3
   </td>
   <td>c13.3:o.3
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.7
   </td>
   <td>
    Unknown data term “unknown:indecipherable”
   </td>
   <td>§4.5.3
   </td>
   <td>c13.3:o.3
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.8
   </td>
   <td>Withheld data term “known:withheld”
   </td>
   <td>§4.5.3
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
  <tr>
   <td>13.9
   </td>
   <td>Information element not applicable
   </td>
   <td>§4.5.3
   </td>
   <td>o
   </td>
   <td>☐
   </td>
  </tr>
</table>



    o.2: It is optional to support one of these items 13.1 and 13.2. \
o.3: IF c13.4, optional to support items 13.5 - 13.7 but all items must be supported.


# 10 Illustrative use cases (informative)

_To do>> include some illustrative use cases here, drawn from real practice to show what information would typically be published for that use case when complying with, for example MIDS level 2._

_Still to do>>_



*   _Levels need to link to user stories: A certain level should be able to serve some specific stories. Analyse MIDS against DiSSCo user stories – see which levels are needed by which user stories to see what this tells us. Cross-refer to Niels article on user stories._
*   _Review levels against ICEDIG Hannu's MS37/D6.5 proposals to ensure we align._


# 11 References

_To do>>Clean up reference list._


            [Brummitt 2001]	Brummitt, R.K. (2001). World Geographical Scheme for Recording Plant Distributions, Edition 2. Biodiversity Information Standards (TDWG). [http://www.tdwg.org/standards/109](http://www.tdwg.org/standards/109).


            [FMI 2018]	Flanders Marine Institute (2018). IHO Sea Areas, version 3. Available online at [http://www.marineregions.org/](http://www.marineregions.org/). doi: [10.14284/323](https://doi.org/10.14284/323).


            [Groom 2019]	Groom G, Dillen M, Hardy H, Phillips S, Willemse L, Wu Z. (2019). Improved standardization of transcribed digital specimen data. Database, Volume 2019, baz129. doi: [10.1093/database/baz129](https://doi.org/10.1093/database/baz129).


            [ISO 3166]	International Standards Organisation (ISO) (2013). ISO 3166. Codes for the Representation of Names of Countries and Their Subdivisions. Part 1: Country codes; Part 2: Country subdivision code; and Part 3: Code for formerly used names of countries. [www.iso.org](http://www.iso.org). 


            [ISO 8601]	International Standards Organisation (ISO) (2019). ISO 8601. Date and Time — Representations for Information Interchange. Part 1: Basic Rules; and Part 2: Extensions. [www.iso.org](http://www.iso.org).  


            [Meyer 2015]	Meyer, Eric T., and Ralph Schroeder. Knowledge machines: digital transformations of the sciences and humanities. MIT Press, 2015.


            [Mons 2017]	Mons B, Neylon CD, Velterop J, Dumontier M, da Silva Santos LOB, Wilkinson M (2017) Cloudy, increasingly FAIR; revisiting the FAIR Data guiding principles for the European Open Science Cloud. Information Services and Use, vol. 37, no. 1, pp. 49-56, 2017. doi: [10.3233/ISU-170824](https://doi.org/10.3233/ISU-170824).


            [Nelson et al. 2015]	Nelson, G., Sweeney, P., Wallace, L. E., Rabeler, R. K., Allard, D., Brown, H., ... & Gilbert, E. (2015). Digitization workflows for flat sheets and packets of plants, algae, and fungi. Applications in Plant Sciences, 3(9), 1500065. doi: [10.3732/apps.1500065](https://doi.org/10.3732/apps.1500065). 


            [RFC 4122]	IETF RFC 4122. (2005). A Universally Unique IDentifier (UUID) URN Namespace. url: [https://www.ietf.org/rfc/rfc4122.txt](https://www.ietf.org/rfc/rfc4122.txt). 


            [Schindel 2018]


            [Webster 2017]


            [Wilkinson 2016]	Wilkinson MD, Dumontier M, Aalbersberg IJ, Appleton G, Axton M, Baak A, Blomberg N, Boiten JW, da Silva Santos LB, Bourne PE, Bouwman J (2016) The FAIR Guiding Principles for scientific data management and stewardship. Scientific data, 3. doi: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)<span style="text-decoration:underline;">.</span>

Brazma et al. 2001 – [https://www.ncbi.nlm.nih.gov/pubmed/11726920](https://www.ncbi.nlm.nih.gov/pubmed/11726920)

Field et al. 2008 – [https://www.nature.com/articles/nbt1360](https://www.nature.com/articles/nbt1360)

Martinez-Bartolomie et al. 2014) – [https://www.ncbi.nlm.nih.gov/pubmed/24136562](https://www.ncbi.nlm.nih.gov/pubmed/24136562)

GRSciColl – [https://www.gbif.org/grscicoll](https://www.gbif.org/grscicoll) 

NEED TO CITE THIS Working Group. Minimum Information for Scientific Collections) / Authority File Working Group (MISC). See [https://www.idigbio.org/wiki/index.php/MISC/Authority-File-Working-Group](https://www.idigbio.org/wiki/index.php/MISC/Authority-File-Working-Group) where you find links to their outputs. It is “does not represent an attempt to establish a community-wide standard for minimum information for scientific collections.” It was an attempt to suggest to data providers what iDigBio would like to see in data provided. Each table also denotes three categories of elements related to successful ingestion, those that are 1) required, 2) highly desired, or 3) complementary. So in this sense, it started to get at what MISC group felt would offer _better practices for discoverability, research use, and linking (use of GUIDs, for example)._

END.

 
