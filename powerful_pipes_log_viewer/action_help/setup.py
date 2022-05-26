import click

from click import Group

from .action import action_help

def setup_action_help(cli: Group):

    @cli.command("help")
    @click.pass_context
    def show_help(ctx):
        """Displays help"""
        action_help(ctx)


__all__ = ("setup_action_help", )
