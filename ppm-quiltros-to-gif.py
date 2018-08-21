import os
from ppm_maker import PPMMaker

input_directory = "sources/ppm/"
output_directory = "generated/images/"
ppm_maker = PPMMaker()
for inputfile in os.listdir(input_directory):
    if inputfile.endswith(".txt"):
        output_filename = os.path.splitext(os.path.basename(inputfile))[0] + ".gif"
        ppm_maker.image_from_ppm_file(input_directory + inputfile, output_directory + output_filename)
        print "Generated " + output_directory + output_filename

