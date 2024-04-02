import amfpy


MOLECULE = "molecule.amf"

amfpy.Reader(MOLECULE)
amfpy.Reader("test.amf")

amfpy.build(animate=False, frate=60)


