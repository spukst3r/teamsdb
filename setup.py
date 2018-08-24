#! /usr/bin/env python

import os

from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='teamsdb-server',
    version='1.0',
    packages=find_packages('teamsdb'),
    package_dir={'': 'teamsdb'},
    include_package_data=True,
)
