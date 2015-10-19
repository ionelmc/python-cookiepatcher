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
import logging
import os
import shutil
import sys
import tempfile

import click
from aspectlib import Aspect
from aspectlib import weave
from cookiecutter.exceptions import InvalidModeException
from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.generate import generate_files
from cookiecutter.main import cookiecutter
from cookiepatcher import __version__

try:
    import ruamel.yaml as yaml
except ImportError:
    import yaml

logger = logging.getLogger(__name__)


def version_msg():
    from cookiecutter.cli import version_msg
    from cookiecutter import __version__

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

    tempdir = tempfile.mkdtemp()

    try:
        os.environ['HOME'] = tempdir
        shutil.copyfile(
            os.path.join(target, '.cookiecutterrc'),
            os.path.join(tempdir, '.cookiecutterrc'),
        )

        with weave(generate_files, save_context):
            cookiecutter(
                template, checkout, no_input,
                overwrite_if_exists=True,
                output_dir=os.path.dirname(target),
            )
    except (OutputDirExistsException, InvalidModeException) as e:
        click.echo(e)
        sys.exit(1)
    finally:
        shutil.rmtree(tempdir)

@Aspect
def save_context(context, **kwargs):
    project_dir = yield
    with open(os.path.join(project_dir, '.cookiecutterrc'), 'w') as fh:
        yaml.safe_dump(fh)
