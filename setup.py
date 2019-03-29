#!/usr/bin/env python

import io
import os
from distutils.core import setup
from glob import glob
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name = 'PasutBIG',
    version = '0.1',
    description = 'Python script for fetching real time tidal observation from Badan Informasi Geospasial (BIG).',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/syahperdana/BIGTIDE',
    email = 'syahperdana@gmail.com',
    author = 'Aldwin Syahperdana',
    license = 'MIT',
    python_requires = '>=2.6.0',
    packages = find_packages(where = 'src'),
    package_dir = {'PasutBIG': 'src/PasutBIG'},
)
