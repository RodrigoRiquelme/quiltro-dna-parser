from ppm_maker import PPMMaker

ppm_maker = PPMMaker("sources/images/quiltro-1.gif")
print(ppm_maker.preview())
print(ppm_maker.output_ppm())
