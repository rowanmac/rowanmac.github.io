import frontmatter
import os
import sys
import yaml

# A function to import individual pages for published material from obsidian,
# extract their YAML data and put them in the correct directory within the JEKYLL site
def importBibliography(YYYYMMFilePath, destinationDirectory):
    articleDirectory = destinationDirectory + "/_articles/"
    bookDirectory = destinationDirectory + "/_books/"
    reviewDirectory = destinationDirectory + "/_reviews/"
    sectionDirectory = destinationDirectory + "/_sections/"


    # List all files in the directory
    workingFiles = []
    if os.path.isdir(YYYYMMFilePath):
        for filename in os.listdir(YYYYMMFilePath):
            file_path = os.path.join(YYYYMMFilePath, filename)
            if os.path.isfile(file_path):
                workingFiles.append(file_path)
    else:
        print(f"Directory {YYYYMMFilePath} does not exist")

    for file in workingFiles:
        with open(file) as f:
            metadata, content = frontmatter.parse(f.read())

        # Ensure 'extra' key exists
        try:
            metadata["extra"]
        except KeyError:
            metadata["extra"] = ""

        # Determine the file type
        fileType = metadata["type"]
        if fileType == "journalArticle" and metadata["extra"] == "review":
            destinationDirectory = reviewDirectory
        elif fileType == "journalArticle":
            destinationDirectory = articleDirectory
        elif fileType == "book":
            destinationDirectory = bookDirectory
        elif fileType == "bookSection":
            destinationDirectory = sectionDirectory
        else:
            print(f"File type {fileType} not recognised")
            sys.exit()

        # Create the yaml header
        yamlHeader = "---\n" + yaml.dump(metadata) + "---\n"

        # Create the markdown file
        outputFilePath = os.path.join(destinationDirectory, os.path.basename(file))
        with open(outputFilePath, 'w') as outputFile:
            outputFile.write(yamlHeader)