#!/usr/bin/python

from ppm_maker import PPMMaker
import sys


def main(argv):
    if len(argv) != 2:
        print("Usage: " + __file__ + " {nombre de archivo}")
        return

    input_file = argv[1]
    ppm_maker = PPMMaker(input_file)
    print(ppm_maker.preview())
    print(ppm_maker.output_ppm())


if __name__ == "__main__":
    main(sys.argv)
