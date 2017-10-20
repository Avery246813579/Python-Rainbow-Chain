from distutils.core import setup
from setuptools import find_packages

setup(
    name='RainbowChain',
    packages=find_packages('lib'),  # this must be the same as the name above
    package_dir={'': 'lib'},
    license="MIT License",
    version='0.2',
    description='Implementing Middle Out (Indexing) to the Markov Chain',
    author='Avery Durrant',
    author_email='avery@frostbyte.co',
    url='https://github.com/Avery246813579/Python-Rainbow-Chain',
    download_url='https://github.com/Avery246813579/Python-Rainbow-Chain/archive/0.5.tar.gz',
    keywords=['Markov Chain', 'Middle Out', 'Markov Model'],
    classifiers=[],
)
