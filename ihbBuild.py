import argparse

from pythonFunctions.importBibliography import importBibliography
from pythonFunctions.importIhb import importIhb
from pythonFunctions.buildDynamicIhb import buildDynamicIhb

parser = argparse.ArgumentParser(description='Input YYYYMM')
parser.add_argument('YYYYMM', type=int, help='YYYYMM')
arg = parser.parse_args()

# File Paths
YYYYMM = arg.YYYYMM
YYYYMMFilePath = "/Users/rowanmacconville/irishHistoryBrief/" + str(YYYYMM) + "/"
DestinationDirectory = "/Users/rowanmacconville/Projects/rowanmac.github.io/my_collections/"

# Possible method of import .bib file and constructing brief from that
#bibFilePath = "/Users/rowanmacconville/Projects/rowanmac.github.io/bibFiles/" + str(YYYYMM) + ".bib"
#importIhb(DestinationDirectory, bibFilePath)

# Import individual bibliography files for published material
#importBibliography(YYYYMMFilePath, DestinationDirectory)

# TODO import ancilliary information (people, publishers, etc.)

# Build the dynamic IHB post
buildDynamicIhb(DestinationDirectory, YYYYMM)