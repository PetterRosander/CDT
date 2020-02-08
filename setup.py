#!/usr/bin/env python

import setuptools as setup

setup.setup(name='cdt',
            version='0.0.0',
            platforms=['unix'],
            install_requires=['pyyaml'],
            scripts=['bin/cdt'],
            packages=setup.find_packages())
