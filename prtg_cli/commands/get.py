import sys
from pprint import pprint

import click


@click.command("get")
@click.argument(
    "resource",
    required=True,
    type=click.Choice(["probes", "groups", "devices", "sensors"]),
)
@click.argument("name", default="*")
@click.pass_obj
def get_command(prtg, resource, name):
    try:
        pprint(prtg.get(resource, name))
    except Exception as e:
        sys.exit(e)
