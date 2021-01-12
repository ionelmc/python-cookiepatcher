"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mcookiepatcher` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``cookiepatcher.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``cookiepatcher.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import io
import logging
import os
import sys
from collections import OrderedDict

import click
from aspectlib import Aspect
from aspectlib import weave
from cookiecutter.config import DEFAULT_CONFIG
from cookiecutter.config import get_config
from cookiecutter.exceptions import InvalidModeException
from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter
from ruamel import yaml

from cookiepatcher import __version__

logger = logging.getLogger(__name__)


def version_msg():
    from cookiecutter import __version__
    from cookiecutter.cli import version_msg

    return 'Cookiepatcher %(version)s from {}; {}'.format(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        version_msg() % dict(version=__version__)
    )


@click.command()
@click.version_option(__version__, '-V', '--version', message=version_msg())
@click.argument('template')
@click.argument('target')
@click.option(
    '--no-input', is_flag=True,
    help='Do not prompt for parameters and only use cookiecutter.json '
         'file content',
)
@click.option(
    '-c', '--checkout',
    help='branch, tag or commit to checkout after git clone',
)
@click.option(
    '-v', '--verbose',
    is_flag=True, help='Print debug information', default=False
)
def main(template, target, no_input, checkout, verbose):
    if verbose:
        logging.basicConfig(
            format='%(levelname)s %(filename)s: %(message)s',
            level=logging.DEBUG
        )
    else:
        logging.basicConfig(
            format='%(levelname)s: %(message)s',
            level=logging.INFO
        )

    try:
        DEFAULT_CONFIG.setdefault('cookiecutter', {})
        src = os.path.join(target, '.cookiecutterrc')
        if os.path.exists(src):
            logger.info("Loading config from %r", src)
            extra_context = get_config(src)
            logger.debug("Loaded %r", extra_context)
            extra_context = extra_context.get('cookiecutter') or extra_context.get('default_context')
            logger.debug("Loaded %r", extra_context)
        else:
            logger.info("No .cookiecutterrc in %r", target)
            extra_context = None

        with weave('cookiecutter.main.generate_files', save_context):
            with weave('cookiecutter.generate.rmtree', complain):
                cookiecutter(
                    template, checkout, no_input,
                    overwrite_if_exists=True,
                    # os.path.dirname does not work with tab-completed (trailing /) paths.
                    # (That's one of the reasons pathlib was created.)
                    output_dir=os.path.abspath(os.path.join(target, os.pardir)),
                    extra_context=extra_context,
                )
    except (OutputDirExistsException, InvalidModeException) as e:
        click.echo(e)
        sys.exit(1)


def complain(func):
    def moan_and_groan(*args, **kwargs):
        raise Exception("Maybe deleting all your shit ain't a good idea ...")

    return moan_and_groan


class Dumper(yaml.SafeDumper):
    pass


Dumper.add_representer(OrderedDict, yaml.Representer.represent_dict)


@Aspect
def save_context(context, **kwargs):
    context = {
        'default_context': {
            key: value
            for key, value in context['cookiecutter'].items()
            if not key.startswith('_')
        }
    }
    project_dir = yield
    with io.open(os.path.join(project_dir, '.cookiecutterrc'), 'w', encoding='utf8') as fh:
        fh.write(u"# Generated by cookiepatcher, a small shim around cookiecutter (pip install cookiepatcher)\n\n")
        try:
            yaml.dump(context, fh, indent=4, width=float('inf'), default_flow_style=False, allow_unicode=True, Dumper=Dumper)
        except Exception as exc:
            logger.exception("Failed yaml.dump with %r", exc)
            raise
