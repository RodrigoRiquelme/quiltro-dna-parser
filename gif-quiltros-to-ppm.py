import os
from ppm_maker import PPMMaker

input_directory = "sources/images/"
output_directory = "generated/ppm/"

for input_file in os.listdir(input_directory):
    if input_file.endswith(".gif"):
        ppm_maker = PPMMaker(input_directory + input_file)
        output_filename = os.path.splitext(os.path.basename(input_file))[0] + ".txt"
        ppm_maker.write_ppm(output_directory + output_filename)
        print "Generated " + output_directory + output_filename
