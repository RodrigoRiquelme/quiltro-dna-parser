from quiltro_dna_parser import QuiltroDnaParser

dna_parser = QuiltroDnaParser("sources/images/quiltro-1.gif")
print(dna_parser.preview())
print(dna_parser.output_ppm())
