# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README') as f:
        return f.read()

setup(name='NoiseTools',
      version='0.3.1.dev0',
      description='Tools for noise analysis',
      long_description=readme(),
      author='Adrian Schlatter',
      author_email='schlatter@phys.ethz.ch',
      url='https://github.com/adrianschlatter/NoiseTools',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Utilities',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7'],
      install_requires=['numpy>=1.8.2,<2'],
      packages=['NoiseTools'])
