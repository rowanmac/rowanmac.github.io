import frontmatter
import os
import sys
import yaml
import re
import sys 
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
            if filename == ".DS_Store":
                continue
            file_path = os.path.join(YYYYMMFilePath, filename)
            if os.path.isfile(file_path):
                workingFiles.append(file_path)
    else:
        print(f"Directory {YYYYMMFilePath} does not exist")

    for file in workingFiles:
        with open(file) as f:
            content = f.read()
            try:
                # Extract YAML front matter
                yaml_content = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL).group(1)
                metadata = yaml.safe_load(yaml_content)
                content = re.sub(r'^---\s*\n(.*?)\n---\s*\n', '', content, flags=re.DOTALL)
            except Exception as e:
                print(f"Error parsing YAML in file {file}: {e}")
                continue            

        # Determine the file type
        fileType = metadata.get("type", "")
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