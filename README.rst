========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github-actions| |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |github-actions| image:: https://github.com/ionelmc/python-cookiepatcher/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/python-cookiepatcher/actions

.. |requires| image:: https://requires.io/github/ionelmc/python-cookiepatcher/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-cookiepatcher/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/cookiepatcher.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/cookiepatcher

.. |wheel| image:: https://img.shields.io/pypi/wheel/cookiepatcher.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/cookiepatcher

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cookiepatcher.svg
    :alt: Supported versions
    :target: https://pypi.org/project/cookiepatcher

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cookiepatcher.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/cookiepatcher

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-cookiepatcher/v0.5.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-cookiepatcher/compare/v0.5.0...master



.. end-badges

Just a small shim around cookiecutter that alters a bit the CLI to work better when reapplying templates to existing
projects. Works best with cookiecutter-pylibrary.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install cookiepatcher

You can also install the in-development version with::

    pip install https://github.com/ionelmc/python-cookiepatcher/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import cookiepatcher
    cookiepatcher.-()


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
