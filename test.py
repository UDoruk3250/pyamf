import amfpy


MOLECULE = "nucleotides.amf"

amfpy.Reader(MOLECULE)

amfpy.animate(10000)
amfpy.build()
