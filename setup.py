# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


# with open('README.rst') as f:
#     readme = f.read()

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='py.project',
    version='1.0.0',
    description='a template py.project',
    long_description=readme,
    author='chrish65535',
    author_email='chrish216_dev@163.com',
    url='https://github.com/chrish65535/py.project',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

