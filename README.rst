=============
Cookiepatcher
=============

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-cookiepatcher/badge/?style=flat
    :target: https://readthedocs.org/projects/python-cookiepatcher
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-cookiepatcher.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-cookiepatcher

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-cookiepatcher?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-cookiepatcher

.. |requires| image:: https://requires.io/github/ionelmc/python-cookiepatcher/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-cookiepatcher/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/python-cookiepatcher/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-cookiepatcher

.. |codecov| image:: https://codecov.io/github/ionelmc/python-cookiepatcher/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-cookiepatcher

.. |landscape| image:: https://landscape.io/github/ionelmc/python-cookiepatcher/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/python-cookiepatcher/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat
    :target: https://www.codacy.com/app/ionelmc/python-cookiepatcher
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/python-cookiepatcher/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/python-cookiepatcher
   :alt: CodeClimate Quality Status
.. |version| image:: https://img.shields.io/pypi/v/cookiepatcher.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/cookiepatcher

.. |downloads| image:: https://img.shields.io/pypi/dm/cookiepatcher.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/cookiepatcher

.. |wheel| image:: https://img.shields.io/pypi/wheel/cookiepatcher.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/cookiepatcher

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cookiepatcher.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/cookiepatcher

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cookiepatcher.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/cookiepatcher

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/python-cookiepatcher/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/python-cookiepatcher/

Just a small shim around cookiecutter that alters a bit the CLI to work better when reapplying templates to existing projects. Works best
with cookiecutter-pylibrary.

* Free software: BSD license

Installation
============

::

    pip install cookiepatcher

Documentation
=============

https://python-cookiepatcher.readthedocs.org/

Development
===========

To run the all tests run::

    tox
