import argparse
import time

from pythonFunctions.importBibliography import importBibliography
from pythonFunctions.importYamlFile import importYamlFile
from pythonFunctions.buildDynamicIhb import buildDynamicIhb

parser = argparse.ArgumentParser(description='Input YAML file to import')
parser.add_argument('YAMLFile', help='YAML file to import')
arg = parser.parse_args()

# File Paths
YAMLFile = arg.YAMLFile
destinationDirectory = "/Users/rowanmacconville/rowanmac.github.io/my_collections/"

# Import individual bibliography files for published material
startTime = time.time()
importYamlFile(destinationDirectory, YAMLFile)
endTime = time.time()
print(f"Bibliography imported successfully in {endTime - startTime:.2f} seconds")

# Build the dynamic IHB post
startTime = time.time()
buildDynamicIhb(destinationDirectory, YAMLFile)
endTime = time.time()
print(f"IHB post built successfully in {endTime - startTime:.2f} seconds")
