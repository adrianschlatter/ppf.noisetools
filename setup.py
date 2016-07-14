# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
# To use a consistent encoding
from codecs import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='NoiseTools',
    version='0.3.1.dev0',
    description='Tools for noise analysis',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/adrianschlatter/NoiseTools',

    # Author details
    author='Adrian Schlatter',
    author_email='schlatter@phys.ethz.ch',

    # Choose your license
    license='Revised BSD',    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Utilities',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'],

    # What does your project relate to?
    keywords='python math noise signal',

    install_requires=['numpy>=1.8.2,<2'],
    extras_require={
        'dev': ['check-manifest'],
        'test': [],
    },

    packages=find_packages(exclude=['docs', 'tests']),

    # Test are in subdir tests/
    test_suite='tests',
    tests_require=[],
)
