# prtg-cli [![PyPi version](https://img.shields.io/pypi/v/prtg-cli.svg)](https://pypi.python.org/pypi/prtg-cli/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/prtg-cli.svg)](https://pypi.python.org/pypi/prtg-cli/) [![](https://img.shields.io/github/license/f9n/prtg-cli.svg)](https://github.com/f9n/prtg-cli/blob/master/LICENSE)

CLI for PRTG Network Monitor

# Installation

```bash
$ pip3 install --user prtg-cli
```

# Setup

For communication with PRTG, use options or set the `PRTG_HOST`, `PRTG_USERNAME`, (`PRTG_PASSWORD` or `PRTG_PASSHASH`) environment variables

# Usage

```bash
$ prtg-cli
Usage: prtg-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --host TEXT      Host of the PRTG
  --username TEXT  Username of the PRTG
  --password TEXT  Password of the PRTG
  --passhash TEXT  Passhash of the PRTG
  --help           Show this message and exit.

Commands:
  duplicate
  get
  object
  passhash
  prtg_version
  sensor_types
  status
  version
```

# Suggestions

- Please use a unique name for `probes`, `groups` and `devices` on PRTG

# Examples

### Information
```bash
### Get all probes
$ prtg-cli get probes
### Get all groups 
$ prtg-cli get groups
### Get specific group
$ prtg-cli get groups <GROUP_NAME>
### Get all devices
$ prtg-cli get devices
### Get specific device
$ prtg-cli get devices <DEVICE_NAME>
```

### Duplication
```bash
### Duplicate a group
$ prtg-cli duplicate group --source <Source_Group> --target <Target_Group> --target-name <New_Group_Name>
### Duplicate a device
$ prtg-cli duplicate device --source <Source_Device> --target-group <Target_Group> --target-name <New_Device_Name> --target-host <New_Device_Host>
```

### Object Manipulation
```bash
### Scan a object
$ prtg-cli object --state scan --resource devices --item <DEVICE_NAME>
### Resume a object
$ prtg-cli object --state resume --resource devices --item <DEVICE_NAME>
### Stop a object
$ prtg-cli object --state stop --resource devices --item <DEVICE_NAME>
### Delete a object
$ prtg-cli object --state delete --resource devices --item <DEVICE_NAME>
```

# Example of Adding Multiple Devices With Config File

```bash
$ cat example.yml
# Device Name
clone: PROD_RABBITMQ_CLUSTER
# Target Group
group: PRTG_CLI

devices:
  - name: CHECKOUT_RMQ_CLUSTER_01
    host: 10.0.20.32

  - name: CHECKOUT_RMQ_CLUSTER_02
    host: 10.0.20.33

$ prtg-cli manager --config-file example.yml
- Create new 'CHECKOUT_RMQ_CLUSTER_01' device
- Create new 'CHECKOUT_RMQ_CLUSTER_02' device
```

# Credits

Thank you for offering fabulous, amazing, incredible rest api at PRTG, it is very nice. :)

https://www.paessler.com/prtg
