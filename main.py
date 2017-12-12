import sys
from scrapper.scrapper import getFreqDict

URL = "http://grist.org/"

def main():
    getFreqDict(URL)

if __name__ == '__main__':
    sys.exit(main())
