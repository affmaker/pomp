# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))


setup(
    name='pomp',
    version=":versiontools:pomp:",
    url='http://bitbucket.org/estin/pomp',
    license='BSD',
    author='Evgeniy Tatarkin',
    author_email='tatarkin.evg@gmail.com',
    description='Screen scraping and web crawling framework',
    long_description=open(os.path.join(here, 'README.rst')).read(),
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    tests_require=['nose >= 1.0', ],
    test_suite='nose.collector',
    setup_requires=['versiontools >= 1.8', ],
    install_requires=['futures', ] if sys.version_info < (3, 2) else [],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
