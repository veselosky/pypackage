#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

# Add all required libraries to requirements.txt
with open('requirements.txt') as f:
    requirements = [line for line in f.read().split('\n') if line]

test_requirements = [
    # TODO: put package test requirements here
]

about = {}
with open("{{ cookiecutter.repo_name }}/__about__.py") as fp:
    exec(fp.read(), about)

# Uncomment if you support 2.6 and use these
# if sys.version_info < (2, 7):
#     requirements += ['argparse']
#     tests_reqs += ['unittest2']

if sys.argv[-1] == 'info':
    for k, v in about.items():
        print('%s: %s' % (k, v))
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme + '\n\n' + history,
    author=about['__author__'],
    author_email=about['__email__'],
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',  # noqa
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={'{{ cookiecutter.repo_name }}':
                 '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=requirements,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
