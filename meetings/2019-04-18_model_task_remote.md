# CD TG Data Model Group Remote Meeting 18/04/2019 14:00 UTC

## Present at meeting
Matt Woodburn, Stan Blum, Quentin Groom, Kate Webbink, Janeen Jones, Sharon Grant, William Ulate, Deborah Paul

## Agenda

1. Introduction to discussion document, followed by feedback and discussion on the approach

2. Define modelling tasks e.g.
    - CDs, relationships and grouping
    - Dimensions
    - Metrics and aggregation

3. Update on use case collection from Deb, and discussion about working up use cases as model requirements and examples

4. Next steps

5. AOB

## Meeting notes

### Agenda items 1 & 2

* (SB) Raised the need for hierarchical structure to be able to distinguish between collections as a whole and different parts of the collection. (MW) The proposed approach allows for hierarchical structures and aggregation within any of the dimensions. (SB) Storage type / collections hierarchy would seem to be a common hierarchy across many use cases. A more structured hierarchical model might fit better, as the dimensional schema-lite approach could be tricky to use. (SG/KW/JJ) The dimensional model seems to be a good fit for the range of CD use cases.
* (QG) Missing from the model are details on tracking CDs (e.g. lumping and splitting) and use of IDs and dates. (SG) Relational model to manage updating and versions over time. (MW) Needs are noted in the discussion doc, but design is an outstanding task.
* (MW) For a given type or scheme of CD, templating could be used to define which dimensions and hierarchies are relevant. (KW) [Whip](https://github.com/inbo/whip), a tool created by Peter Desmet, may be a good tool for this. (QG) Working with Anton Güntsch on the possibility of setting up a Wikibase instance for the community to support designing and testing models with real or imagined data. Currently at a conceptual stage. **AP: QG to invite MW to web meeting discussing Wikibase**
* (SG) Field Museum and David Bloom have been working up a proposal for a CD use case for grouped collections (https://docs.google.com/document/d/13intzQGmcqvOpdWUyaGQHl-GEgs_sHPWy1-MBdIrIT4), and considering which dimensions the use case would need.

### Agenda item 3

* (DP) Asked for feedback on the possible templates for carrying out the use case breakdowns. Consensus was that the simpler format was preferred. (SB) Extract the basic data modelling structure for the use case e.g. cardinality, tracking collection changes over time, minimum specs for data elements. (MW) Identify the dimensions and metrics required for each use case.
* (SB) Has drafted a [Concept of Operations document](https://docs.google.com/document/d/1i7BI_HI27iDw4eIlUPP7jEZIv3XPQU8xb53zTNfiwsM) for CDs, referencing requirements at a higher level than use cases. **AP: All to review and comment**

### Agenda item 4

* **AP: SB to work up the more hierarchical model to share with the group**
* **AP: DP will post the use case review model request**
* **AP: SG/KW/JJ/DB to put some time into fitting the use case to the current model to check fit. However, suggestion was to limit to a few hours pending the assessment of SB's alternative suggestion.**

### Agenda item 5

* QG demonstrated an example of how Wikibase can be used for modelling and testing data. 