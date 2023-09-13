import amfpy


MOLECULE = "molecule.amf"

amfpy.Reader(MOLECULE)

amfpy.build(animate=True, frate=1200)
