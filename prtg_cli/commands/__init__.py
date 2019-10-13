from pprint import pprint

import click

from .duplicate import duplicate_command
from .get import get_command
from .object import object_command


@click.command("prtg_version")
@click.pass_obj
def prtg_version_command(prtg):
    prtg_version = prtg.version()
    click.echo(f"Prtg Version: {prtg_version}")


@click.command("passhash")
@click.pass_obj
def passhash_command(prtg):
    click.echo(f"Passhash: {prtg.passhash()}")


@click.command("status")
@click.pass_obj
def status_command(prtg):
    result = prtg.status()
    pprint(result)


@click.command("sensor_types")
@click.pass_obj
def sensor_types_command(prtg):
    sensor_types = prtg.sensor_types()
    pprint(sensor_types)
