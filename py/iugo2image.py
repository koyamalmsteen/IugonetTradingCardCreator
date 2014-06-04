#!/usr/bin/env python
import urllib
import os

try:
    import lxml.etree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import optparse
import sys
import Image

def main():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input', 
                      dest="inputXml",
                      default="../xml/VHF.xml",
                      help="(in XML)")
    parser.add_option('-o', '--output',
                      dest="output_filename",
                      default="/tmp/qrcode.png",
                      help="(in PNG)")
    options, remainder = parser.parse_args()

    tree = ET.parse(options.inputXml)
    elem = tree.getroot()

    id = elem.find('.//{http://www.iugonet.org/data/schema}Instrument/{http://www.iugonet.org/data/schema}ResourceID').text

    baseWidth = 300
    baseHeight = 150

    imageURL = "http://center.stelab.nagoya-u.ac.jp/sd2007/top.jpg"
    imageFile = "/tmp/hoge.jpg"
    urllib.urlretrieve(imageURL, imageFile)
    img_orig = Image.open(imageFile)

    # ignore the aspect ratio
    img_resized = img_orig.resize((baseWidth,baseHeight), Image.ANTIALIAS)
    img_resized.save("/tmp/hoge2.jpg")

    os.remove(imageFile)

if __name__ == "__main__":
    main()
