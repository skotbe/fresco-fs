#!/usr/bin/env python
from setuptools import setup
import os
import re


VERSIONFILE = "fresco_fs.py"


def get_version():
    return re.search("^__version__\s*=\s*['\"]([^'\"]*)['\"]",
                     read(VERSIONFILE),
                     re.M).group(1)


def read(*path):
    with open(os.path.join(os.path.dirname(__file__), *path), 'rb') as f:
        return f.read().decode('UTF-8')


setup(name='fresco-fs',
      version='0.1.dev0',
      description='Filesystem resources for fresco',
      long_description=read('README.rst') + "\n\n" + read("CHANGELOG.rst"),
      url='https://skot.be/',
      author='Oliver Cope',
      author_email='oliver@redgecko.org',
      license='Apache',
      install_requires=['fresco'],
      py_modules=['fresco_fs'],
      packages=[])
