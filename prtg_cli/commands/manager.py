import io
import sys

import click
import yaml
from jsonschema import validate

CONFIG_FILE_SCHEMA = """
type: object
properties:
  clone:
    type: string
  group:
    type: string
  devices:
    type: array
    items:
      type: object
      properties:
        name:
          type: string
        host:
          type: string
"""


@click.command("manager")
@click.option("--config-file", required=True)
@click.pass_obj
def manager_command(prtg, config_file):
    try:
        with io.open(config_file, "r") as f:
            data = yaml.safe_load(f)
            validate(data, yaml.safe_load(CONFIG_FILE_SCHEMA))
            clone_name = data["clone"]
            group_name = data["group"]
            devices = data["devices"]

            clone = prtg.get("devices", clone_name)
            clone_id = clone["objid"]
            group = prtg.get("groups", group_name)
            group_id = group["objid"]

            for device in data["devices"]:
                name = device["name"]
                host = device["host"]
                print(f"- Create new '{name}' device")
                prtg.duplicate_device(
                    source=clone_id,
                    target_group=group_id,
                    target_name=name,
                    target_host=host,
                )

    except Exception as e:
        sys.exit(e)
