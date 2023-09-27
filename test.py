import amfpy


MOLECULE = "molecule.amf"

amfpy.Reader(MOLECULE)

amfpy.build(animate=False, frate=120)
