import os
from ppm_maker import PPMMaker

input_directory = "sources/images/"
output_directory = "generated/ppm/"

for inputfile in os.listdir(input_directory):
    if inputfile.endswith(".gif"):
        ppm_maker = PPMMaker(input_directory + inputfile)
        output_filename = os.path.splitext(os.path.basename(inputfile))[0] + ".txt"
        ppm_maker.write_ppm(output_filename)
        print "Generated " + output_directory + output_filename
