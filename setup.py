# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

with open(os.path.join(os.path.dirname(__file__),
                       'json2data/__init__.py')) as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='json2data',
    version=version,
    description='Generatre Json data to Excel',
    long_description=readme,
    author='jeffrey',
    author_email='jeffrey0702@gmail.com',
    url='https://github.com/jeffreydong/json2data',
    license=license,
    packages=[
        'json2data',
    ],
    package_dir={'json2data':'json2data'},
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)

