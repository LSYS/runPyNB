#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import re

from setuptools import setup

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

install_requires = ['nbformat', 'nbconvert']
setup(
    name="runpynb",
    version="0.2.0",
    license='MIT',
    author="Lucas Shen",
    author_email="lucas@lucasshen.com",
    maintainer="Lucas Shen",
    maintainer_email="lucas@lucasshen.com",    

    url="https://github.com/lsys/runPyNB",
    description="Run (and time) Jupyter Notebooks for command-line and makefile",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=["runpynb"],
    scripts=["runpynb/scripts/runpynb"],
    install_requires=install_requires,
    keywords=['jupyter notebook', 'jupyter', 'command-line', 'makefile', 'make', 'nbconvert'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',    
        'Programming Language :: Python :: 3.8',    
        'Programming Language :: Python :: 3.9',    
        'Programming Language :: Python :: 3.10',    
        ],
)
