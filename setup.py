import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

LONG_DESC = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

setup(
    name = "ghp-update",
    version = "0.1",
    description = "Update your github account or organization pages repository",
    long_description = LONG_DESC,
    author = "Julien Seiler",
    author_email = "julien.seiler@gmail.com",
    license = "GNU GENERAL PUBLIC LICENSE v2",
    url = "http://github.com/coalkids/ghp-update",
    zip_safe = False,

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
    ],

    scripts = ['ghp-update']
)