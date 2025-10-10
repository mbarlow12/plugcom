from typing import MutableMapping

import click

from plugcom.core import hookimpl


@click.command(name="run")
def subcommand():
    click.echo(f"I was called from {__name__}.")


@hookimpl
def plugcom_add_command(cmd_dict: MutableMapping[str, click.Command]):
    cmd_dict["run"] = subcommand
