# -*- coding: utf-8 -*-
# (c) Copyright 2019 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
import os
import re


# Read version number from version.py
version_line = open("circuitpython_sensirion_i2c_driver/version.py", "rt").read()
result = re.search(r"^version = ['\"]([^'\"]*)['\"]", version_line, re.M)
if result:
    version_string = result.group(1)
else:
    raise RuntimeError("Unable to find version string")


# Use README.rst and CHANGELOG.rst as package description
root_path = os.path.dirname(__file__)
readme = open(os.path.join(root_path, 'README.rst')).read()
changelog = open(os.path.join(root_path, 'CHANGELOG.rst')).read()
long_description = readme.strip() + "\n\n" + changelog.strip() + "\n"


setup(
    name='circuitpython-sensirion-i2c-driver',
    version=version_string,
    author='Sensirion',
    author_email='info@sensirion.com',
    description='Base Driver for Communicating With I2C Devices',
    license='BSD',
    keywords='sensirion i2c driver',
    url='https://github.com/good-enough-technology/CircuitPython_sensirion_i2c_driver',
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    python_requires='>=3.5',
    install_requires=[
    ],
    extras_require={
        'test': [
            'flake8~=3.7.8',
            'mock~=3.0.0',
            'pytest~=6.2.5',
            'pytest-cov~=3.0.0',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Hardware :: Hardware Drivers'
    ]
)
