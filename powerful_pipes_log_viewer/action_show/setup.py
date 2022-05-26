import click

from click import Group

from powerful_pipes_log_viewer import add_shared_arguments

from .action import action_show
from .models import RunningConfigShow

def setup_action_show(cli: Group):

    @cli.command("show")
    @click.option(
        "-n", "--log-entry",
        default=None,
        type=int,
        help="display specific entry number"
    )
    @click.pass_context
    def show_entry(ctx, **kwargs):
        """Show log entry details"""
        config = RunningConfigShow(**kwargs)

        action_show(config)

    add_shared_arguments(show_entry)

__all__ = ("setup_action_show", )
