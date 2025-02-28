import re
import argparse
import os

# A program to convert the inline footnotes in a markdown file to Jekyll includes and autogenerate a bibliography

def convertFootnotes(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()

    pattern = re.compile(r'^\[\^(\d+)\]: (.*)')
    wordPattern = re.compile(r'\[[(\w+)\]]')

    with open(filePath, 'w') as file:
        for line in lines:
            match = pattern.match(line)
            if match:
                footnoteContent = match.group(2)
                convertedContent = wordPattern.sub(r"{%- include footnote.html id='/\1' %}", footnoteContent)
                newLine = f"[^{match.group(1)}]: {convertedContent}\n"
                file.write(newLine)
            else:
                file.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input md file to convert footnotes')
    parser.add_argument('mdFile', help='Markdown file to convert footnotes')
    arg = parser.parse_args()
    mdFile = arg.mdFile

    targetDirectory = "/Users/rowanmacconville/rowanmac.github.io/my_collections/_posts/"
    filePath = os.path.join(targetDirectory, mdFile)
    convertFootnotes(filePath)