========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |appveyor| |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.org/ionelmc/python-cookiepatcher.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-cookiepatcher

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-cookiepatcher?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-cookiepatcher

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-cookiepatcher/v0.4.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-cookiepatcher/compare/v0.4.0...master



.. end-badges

Just a small shim around cookiecutter that alters a bit the CLI to work better when reapplying templates to existing
projects. Works best with cookiecutter-pylibrary.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install cookiepatcher

Documentation
=============

Usage: ``cookiepatcher [OPTIONS] TEMPLATE TARGET``

Args:

.. list-table::
    :stub-columns: 1

    * - ``TARGET``
      - Directory where to look for ``.cookiecutterrc``.
    * - ``TEMPLATE``
      - Name of cookiecutter template.


Options:

  -V, --version        Show the version and exit.
  --no-input           Do not prompt for parameters and only use
                       cookiecutter.json file content
  -c, --checkout TEXT  branch, tag or commit to checkout after git clone
  -v, --verbose        Print debug information
  --help               Show this message and exit.


Development
===========

To run the all tests run::

    tox
