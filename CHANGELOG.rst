
Changelog
=========

0.4.0 (2020-11-06)
------------------

* Fixed the ``.cookiecutterrc`` save code so that:

  * ``default_context`` is the root key (instead of ``cookiecutter``).
  * underscore prefixed keys are stripped (they are cookiecutter internals).
* Made `3.5` the minimum Python version.

0.3.4 (2020-04-05)
------------------

* Fixed ``.cookiecutterrc`` being dumped with ``!!omap`` garbage.

0.3.3 (2017-10-25)
------------------

* Fixed issues with god knows what changed again in cookiecutter.

0.3.2 (2017-07-19)
------------------

* Fixed issues with linewrapping in ``.cookiecutterrc``.

0.3.1 (2017-07-19)
------------------

* Fixed more breakage.


0.3.0 (2015-11-28)
------------------

* Fix issues with Python 2.7.

0.3.0 (2015-11-28)
------------------

* Fix issues with Python 2.7.

0.2.0 (2015-11-19)
------------------

* Removed some workarounds. Requires ``cookiecutter>=1.3.0``.

0.1.1 (2015-11-05)
------------------

* Force `utf8` in various places.

0.1.0 (2015-10-19)
------------------

* First release on PyPI.
