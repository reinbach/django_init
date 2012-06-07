#!/usr/bin/env python
from setuptools import setup

requires = [
    'Django==1.4',
    'psycopg2==2.4.5',
    'Jinja2==2.6',
    'Coffin==0.3.6',
    'Fabric==1.4.2',
]

setup(
    name='<project_name>',
    version='1.0',
    description='<project_name> description',
    author='Greg Reinbach',
    author_email='greg@reinbach.com',
    url='http://github.com/<project_name>',
    install_requires=requires,
)