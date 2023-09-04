import amfpy


MOLECULE = "nucleotides.amf"

amfpy.Reader(MOLECULE)

amfpy.build(animate=True, frate=10000)
