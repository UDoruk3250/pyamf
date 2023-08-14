from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'Absolute Molecule File library extension for python'
LONG_DESCRIPTION = 'Absolute Molecule File library extension for python. Absolute Molecule File'

setup(name='amfpy-python',
      version=VERSION,
      author='Doruk Alp Uzunarslan',
      author_email='duzunarslan27@my.uaa.k12.tr',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      packages=find_packages(),
      install_requires=['matplotlib'],
      keywords=['python', 'modelling', 'molecule', 'atom', 'molecular modelling'])
