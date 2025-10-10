
from typing import MutableMapping
from click import Command
from plugcom.core import hookspec


@hookspec
def plugcom_add_command(cmd_dict: MutableMapping[str, Command]):
    """Define your subcommand and add it to the dictionary"""
    ...
