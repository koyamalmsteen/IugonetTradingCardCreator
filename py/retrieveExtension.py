#!/usr/bin/env python
from xml.etree import ElementTree
import getopt, sys, Image

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

    FILE = "qrcode.png"

    Image.open(FILE).resize((300,150)).save("qrcode2.png")

if __name__ == "__main__":
    main()
