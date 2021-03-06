#!/usr/bin/env python
try:
    import lxml.etree as ET
except AttributeError:
    def register_namespace(prefix, uri):
        ET._namespace_map[uri] = prefix
#except ImportError:
#    import xml.etree.ElementTree as ET
import qrcode.image.base

import optparse
import sys
import qrcode
import qrcode.image.svg

def main():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input', 
                      dest="input_filename",
                      default="../xml/VHF.xml",
                      help="(in XML)")
    parser.add_option('-o', '--output',
                      dest="output_filename",
                      default="/tmp/qrcode.png",
                      help="(in PNG)")
    options, remainder = parser.parse_args()

    tree = ET.parse(options.input_filename)
    elem = tree.getroot()

    id = elem.find('.//{http://www.iugonet.org/data/schema}Instrument/{http://www.iugonet.org/data/schema}ResourceID').text

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
        )
    qr.add_data(id)
    qr.make(fit=True)
    img = qr.make_image()
#    img = qrcode.make(id)
    img.save(options.output_filename)


if __name__ == "__main__":
    main()
