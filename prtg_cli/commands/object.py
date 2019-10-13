import sys

import click


@click.command("object")
@click.option(
    "--state", required=True, type=click.Choice(["resume", "pause", "delete", "scan"])
)
@click.option(
    "--resource",
    required=True,
    type=click.Choice(["probes", "groups", "devices", "sensors"]),
)
@click.option("--item", required=True, help="name or id")
@click.pass_obj
def object_command(prtg, state, resource, item):
    try:
        if prtg.object_state(state, resource, item) == 200:
            click.secho('Success', fg='green')
        else:
            click.secho('Error', fg='red')
    except Exception as e:
        sys.exit(e)
