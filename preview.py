#!/usr/bin/python

from quiltro_dna_parser import QuiltroDnaParser
import sys


def main(argv):
    if len(argv) != 2:
        print("Usage: " + __file__ + " {nombre de archivo}")
        return

    input_file = argv[1]
    dna_parser = QuiltroDnaParser(input_file)
    print(dna_parser.preview())
    print(dna_parser.output_ppm())


if __name__ == "__main__":
    main(sys.argv)
