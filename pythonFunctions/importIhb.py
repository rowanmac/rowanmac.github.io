import os
import bibtexparser
import yaml

# A function to create the IHB post file from an .bib file exported from Zotero
# Workings assuming the .bib file is named YYYYMM.bib

def importIhb(destinationDirectory, bibFilePath):
    ihbDirectory = destinationDirectory + "/_posts/"

    if not os.path.exists(bibFilePath):
        print(f"Bib file {bibFilePath} does not exist")
        return
    
    library = bibtexparser.parse_file(bibFilePath)
    if len(library.failed_blocks) > 0:
        print(f"Some blocks failed to parse. {library.failed_blocks}.")
    else:
        print("All blocks parsed successfully")

    for entry in library.entries:
        keyValueDict = {
            "citeKey": entry.key
        }
        for field in entry.fields:
            keyValueDict[field.key] = field.value
        

    return