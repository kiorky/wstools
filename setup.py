#!/usr/bin/env python
#
# $Id: setup.py,v 1.11 2005/02/15 16:32:22 warnes Exp $

import os,re
from setuptools import setup, find_packages

__version__ = '0.2'


url="http://pywebsvcs.sf.net/"


def read(*rnames):
    return "\n"+ open(
        os.path.join('.', *rnames)
    ).read()

long_description="""WSDL parsing services package for Web Services for Python. see """ + url \
    + read('README.txt')\
    + read('CHANGES.txt')\


setup(
    name="wstools",
    version=__version__,
    description="wstools",
    maintainer="Gregory Warnes, kiorky",
    maintainer_email="Gregory.R.Warnes@Pfizer.com, kiorky@cryptelium.net",
    url = url,
    long_description=long_description,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True, 
    install_requires=[]
)

