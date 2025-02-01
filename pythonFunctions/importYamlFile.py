import os
import yaml
import argparse

def importYamlFile(destinationDirectory, YYYYMM):
    # File Paths
    articleDirectory = destinationDirectory + "/_articles/"
    bookDirectory = destinationDirectory + "/_books/"
    reviewDirectory = destinationDirectory + "/_reviews/"
    sectionDirectory = destinationDirectory + "/_sections/"
    yamlFilePath = os.path.join("/Users/rowanmacconville/Projects/rowanmac.github.io/yamlFiles/" + f"{YYYYMM}.yaml")

    if not os.path.exists(yamlFilePath):
        print(f"YAML file {yamlFilePath} does not exist")
        return

    with open(yamlFilePath, 'r') as yamlFile:
        data = yaml.safe_load(yamlFile)
    
    references = data.get('references', [])
    for reference in references:

        # Adds extra Yaml info
        reference["category"] = int(YYYYMM)
        reference["layout"] = "page"
        reference["externalUrl"] = reference.get("URL")
        reference["permalink"] = "/" + reference.get("citation-key", "")

        # Unpacks note section into new fields
        notes = reference.get("note", "").splitlines()
        for note in notes:
            note = note.split(":")
            reference[note[0]] = "".join(note[1:]).strip()
        reference.pop("note", None)

        # Converts chapter type to section
        if reference.get("type", "") == "chapter":
            reference["type"] = "section"
            reference["chapter"] = int(reference["chapter"])
        
        try:
            reference["review"]
        except KeyError:
            reference["review"] = "false"

        fileType = reference.get("type", "")
        if reference["review"] == "true":
            reference["type"] == "review"
            destinationDirectory = reviewDirectory
            template = "{% include reviewPageTemplate.html %}"
        elif fileType == "article-journal":
            destinationDirectory = articleDirectory
            template = "{% include articlePageTemplate.html %}"
        elif fileType == "book":
            destinationDirectory = bookDirectory
            template = "{% include bookPageTemplate.html %}"
        elif fileType == "section":
            destinationDirectory = sectionDirectory
            template = "{% include sectionPageTemplate.html %}"
        else:
            print(f"File type {fileType} not recognised")
            continue

        # Create the yaml header
        yamlHeader = "---\n" + yaml.dump(reference) + "---\n"

        # Create the markdown file
        outputFilePath = os.path.join(destinationDirectory, reference["citation-key"] + ".md")
        with open(outputFilePath, 'w') as outputFile:
            outputFile.write(yamlHeader + template)
    return True