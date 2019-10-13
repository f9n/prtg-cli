import os
import sys

import click

from . import __version__
from .commands import (
    get_command,
    duplicate_command,
    object_command,
    prtg_version_command,
    passhash_command,
    status_command,
    sensor_types_command,
)
from .core import Prtg, PrtgConfig


@click.group()
@click.option("--host", envvar="PRTG_HOST", help="Host of the PRTG")
@click.option("--username", envvar="PRTG_USERNAME", help="Username of the PRTG")
@click.option("--password", envvar="PRTG_PASSWORD", help="Password of the PRTG")
@click.option("--passhash", envvar="PRTG_PASSHASH", help="Passhash of the PRTG")
@click.pass_context
def main(ctx, host, username, password, passhash):
    try:
        prtg_config = PrtgConfig(
            host=host, username=username, password=password, passhash=passhash
        )
    except Exception as e:
        sys.exit(e)

    ctx.obj = Prtg(config=prtg_config)


@main.command("version")
def version_cmd():
    click.echo(f"prtg-cli: {__version__}")


main.add_command(get_command)
main.add_command(duplicate_command)
main.add_command(object_command)
main.add_command(status_command)
main.add_command(sensor_types_command)
main.add_command(prtg_version_command)
main.add_command(passhash_command)
