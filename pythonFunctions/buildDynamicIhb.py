import yaml
import os
from datetime import datetime
import calendar

def buildDynamicIhb(destinationDirectory, YYYYMM):
    destinationDirectory = destinationDirectory + "/_posts/"

    briefYear = datetime.now().year
    briefMonth = datetime.now().month
    briefDay = datetime.now().day
    postFileName = f"{briefYear}-{briefMonth}-{briefDay}-ihb.md"
    postFilePath = os.path.join(destinationDirectory, postFileName)

    postTitle = f"Irish History Brief for {calendar.month_name[int(str(YYYYMM)[-2:])]} {str(YYYYMM)[:4]}"

    # Create YAML header
    yamlHeaderDict = {
        'layout': 'post',
        'title': postTitle,
        'date': f"{briefYear}-{briefMonth}-{briefDay}",
    }
    yamlHeader = "---\n" + yaml.dump(yamlHeaderDict) + "---\n"

    with open(postFilePath, 'w') as outputFile:
            outputFile.write(yamlHeader)
    return