import yaml
import argparse
import os

parser = argparse.ArgumentParser(description='Input YAML file to import')
parser.add_argument('YAMLFile', help='YAML file to import')
arg = parser.parse_args()

YAMLFile = arg.YAMLFile
yamlFilePath = os.path.join("/Users/rowanmacconville/rowanmac.github.io/yamlFiles/" + f"{YAMLFile}.yaml")

if not os.path.exists(yamlFilePath):
    print(f"YAML file {yamlFilePath} does not exist")
    sys.exit()

with open(yamlFilePath, 'r') as yamlFile:
    data = yaml.safe_load(yamlFile)

# Initialising contents
booksList = []
booksListMarkdown = "# Books\n---\n"
articlesList = []
articlesListMarkdown = "# Articles\n---\n"
reviewsList = []
reviewsListMarkdown = "# Reviews\n---\n"

references = data.get('references', [])
for reference in references:
    if reference["type"] == "book":
        booksList.append(reference)
    elif reference["type"] == "article-journal" and reference["note"] not 
        articlesList.append(reference)
    else:
        reviewsList.append(reference)