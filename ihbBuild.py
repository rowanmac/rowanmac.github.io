import argparse
import time

from pythonFunctions.importBibliography import importBibliography
from pythonFunctions.importYamlFile import importYamlFile
from pythonFunctions.buildDynamicIhb import buildDynamicIhb

parser = argparse.ArgumentParser(description='Input YYYYMM')
parser.add_argument('YYYYMM', type=int, help='YYYYMM')
arg = parser.parse_args()

# File Paths
YYYYMM = arg.YYYYMM
destinationDirectory = "/Users/rowanmacconville/Projects/rowanmac.github.io/my_collections/"

# Import individual bibliography files for published material
startTime = time.time()
importYamlFile(destinationDirectory, YYYYMM)
endTime = time.time()
print(f"Bibliography imported successfully in {endTime - startTime:.2f} seconds")

# TODO import ancilliary information (people, publishers, etc.)

# Build the dynamic IHB post
startTime = time.time()
#buildDynamicIhb(destinationDirectory, YYYYMM)
endTime = time.time()
print(f"IHB post built successfully in {endTime - startTime:.2f} seconds")
