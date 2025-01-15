import argparse

from pythonFunctions.importBibliography import importBibliography

parser = argparse.ArgumentParser(description='Input YYYYMM')
parser.add_argument('YYYYMM', type=int, help='YYYYMM')
arg = parser.parse_args()

# File Paths
YYYYMM = arg.YYYYMM
YYYYMMFilePath = "/Users/rowanmacconville/irishHistoryBrief/" + str(YYYYMM) + "/"
destinationDirectory = "/Users/rowanmacconville/Projects/rowanmac.github.io/my_collections/"

# Import individual bibliography files for published material
importBibliography(YYYYMMFilePath, destinationDirectory)

# TODO import ancilliary information (people, publishers, etc.)

# TODO Compile IHB file