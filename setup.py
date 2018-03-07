#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

VERSION='0.1'
BUILD = os.environ.get('BUILD') or '0'

packages = [
    'invoice_ocr',
]

package_data = {
}

requires = [
    'requests',
    'ruamel.yaml'
]

tests_requires = [
    'pytest'
]

classifiers = [
        'Development Status:: 2 - Pre - Alpha',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='invoice-ocr',
    version=VERSION + '.' + BUILD,
    description='Invoice OCR Application',
    long_description=readme,
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    author='Samuel Tin',
    author_email='samuel.tin@gmail.com',
    license='Proprietary',
    classifiers=classifiers,
    setup_requires=['pytest-runner'],
    tests_require=tests_requires
)
