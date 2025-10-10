
import click

from plugcom.core.cli.plugcom_group import PlugcomGroup


@click.command(cls=PlugcomGroup)
@click.version_option()
@click.pass_context
def main(ctx: click.Context):
    pass

