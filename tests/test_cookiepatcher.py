
from click.testing import CliRunner

from cookiepatcher.__main__ import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])

    assert result.output == '''Usage: main [OPTIONS] TEMPLATE TARGET

Options:
  -V, --version        Show the version and exit.
  --no-input           Do not prompt for parameters and only use
                       cookiecutter.json file content
  -c, --checkout TEXT  branch, tag or commit to checkout after git clone
  -v, --verbose        Print debug information
  --help               Show this message and exit.
'''
    assert result.exit_code == 0
