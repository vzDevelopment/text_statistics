#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""Script for packaging text_statistics module."""

from setuptools import setup

with open('README.md', 'r') as file_handle:
    long_description = file_handle.read()

setup(
    name='text_statistics',
    description='A libary to produce statistics for text files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Vince Zarola',
    version='0.1.0',
    packages=['text_statistics'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
