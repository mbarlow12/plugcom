from typing import MutableMapping
from plugcom.core import hookimpl
import click

@hookimpl
def plugcom_add_command(cmd_dict: MutableMapping[str, click.Command]):

    cmd_name = "doit"

    @click.command(name=cmd_name)
    @click.option("--foo", "-f", type=str, default="I am the default.")
    def my_sub_cmd(foo: str):
        click.echo(f"you passed in {foo}")

    cmd_dict[cmd_name] = my_sub_cmd
