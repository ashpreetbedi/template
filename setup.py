# -*- coding: utf-8 -*-

from setuptools.command.test import test as TestCommand
from setuptools import setup
import os
import sys
import template

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='template',
    version='0.1.0',
    url='',
    license=license,
    author='Ashpreet Bedi',
    author_email='ashpreetbedi@hotmail.com',
    tests_require=['pytest'],
    install_requires=['requests', 'pytest'],
    cmdclass={'test': PyTest},
    description='Sample package template',
    long_description=readme,
    packages=['template'],
)
