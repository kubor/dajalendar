#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup.py
"""

from setuptools import setup, find_packages

setup(
    name='dajalendar',
    version='0.1',
    description='show calendar and dajare',
    author='kubor',
    author_email='rkubo.4w@gmail.com',
    url='https://github.com/kubor',
    license='Copyright(c) 2015 kubor. MIT-Licence',
    packages=['dajalendar'],
    package_dir={'dajalendar': 'dajalendar'},
    package_data={
        'dajalendar': ['data/*.json'],
    },
    entry_points={
        'console_scripts': [
            'dajalendar=dajalendar.dajalendar:main',
        ]
    },
)
