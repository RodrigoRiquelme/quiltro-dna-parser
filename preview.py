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


if __name__ == "__main__":
    print "main"
    main(sys.argv)
