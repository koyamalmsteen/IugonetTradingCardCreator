#!/usr/bin/env python
from xml.etree import ElementTree
import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-o", "--output"):
            output = a

    XMLFILE = "VHF.xml"

    tree = ElementTree.parse(XMLFILE)
    elem = tree.getroot()
    print elem

    e = elem.find('.//{http://www.iugonet.org/data/schema}Version')
    print e.text

if __name__ == "__main__":
    main()
