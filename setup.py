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
    package_dir = {'': 'src'},
    py_modules = [splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data = True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[
        'Pasut', 'BIG', 'Pasang Surut',
    ],
)
