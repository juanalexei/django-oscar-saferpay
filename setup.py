#!/usr/bin/env python

from saferpay_oscar import VERSION
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='django-oscar-saferpay',
    packages=find_packages(),
    version=VERSION,
    license='MIT',
    description='Saferpay payment dashboard for django-oscar.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yves Serrano',
    author_email='ys@taywa.ch',
    url='https://github.com/taywa/django-oscar-saferpay',
    keywords=['saferpay', 'payment'],
    install_requires=[
        'Django>=1.11,<3.2',
        'django-saferpay>=0.1',
        'django-oscar>=1.6',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 3.1',
    ],
)
