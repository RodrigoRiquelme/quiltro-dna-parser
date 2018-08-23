#!/usr/bin/python

import os
import sys

from quiltro_dna_parser import QuiltroDnaParser


def main(argv):
    if len(argv) != 3:
        print("Usage: " + __file__ + " {filename} {ppm string}")
        return

    ppm_input = argv[1]
    output_filename = argv[2]

    dna_parser = QuiltroDnaParser()
    if os.path.isfile(ppm_input):
        print "Generating " + output_filename + " from file " + ppm_input
        dna_parser.image_from_ppm_file(ppm_input, output_filename)
    else:
        print "Generating " + output_filename + " from string '" + ppm_input + "'"
        dna_parser.image_from_ppm(ppm_input, output_filename)


if __name__ == "__main__":
    main(sys.argv)
