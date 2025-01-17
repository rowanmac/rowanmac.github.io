# Irish History Brief Web Implementation

## Generating the Brief
### Sections
#### Section ordering
Sections are ordered using the number stored in the `extra:` field.
A preface or introduction without chapter numbering is `extra: 0` and a conclusion without chapter numbering is `extra: 1000`
### Reviews
#### Fixing Zotero Metadata
Data needed including review tag, works reviewed and the citekey of works reviewed is all included in the extra section of Zotero data each item separated using %%% in this pattern review%%%firstWordReviewedName by Author%%%firstWorkCitekey%%%secondWorkName by Author%%%secondWordCitekey