import sys

import click


@click.group("duplicate")
def duplicate_command():
    pass


@duplicate_command.command("device")
@click.option("--source", required=True)
@click.option("--target-group", required=True)
@click.option("--target-name", required=True, type=str)
@click.option("--target-host", required=True, type=str)
@click.pass_obj
def duplicate_device(prtg, source, target_group, target_name, target_host):
    try:
        if prtg.duplicate_device(source, target_group, target_name, target_host) == 200:
            click.secho('Success', fg='green')
        else:
            click.secho('Error', fg='red')
    except Exception as e:
        sys.exit(e)


@duplicate_command.command("group")
@click.option("--source", required=True)
@click.option("--target", required=True)
@click.option("--target-name", required=True, type=str)
@click.pass_obj
def duplicate_group(prtg, source, target, target_name):
    try:
        if prtg.duplicate_group(source, target, target_name) == 200:
            click.secho('Success', fg='green')
        else:
            click.secho('Error', fg='red')
    except Exception as e:
        sys.exit(e)


@duplicate_command.command("sensor")
@click.option("--source", required=True)
@click.option("--target-device", required=True)
@click.option("--target-name", required=True, type=str)
@click.pass_obj
def duplicate_sensor(prtg, source, target_device, target_name):
    click.echo("@TODO")
