import os
from quiltro_dna_parser import QuiltroDnaParser

input_directory = "sources/images/"
output_directory = "generated/ppm/"

for input_file in os.listdir(input_directory):
    if input_file.endswith(".gif"):
        dna_parser = QuiltroDnaParser(input_directory + input_file)
        output_filename = os.path.splitext(os.path.basename(input_file))[0] + ".txt"
        dna_parser.write_ppm(output_directory + output_filename)
        print "Generated " + output_directory + output_filename
