import click

from click import Group

from powerful_pipes_log_viewer import add_shared_arguments

from .action import action_list
from .models import RunningConfigList

def setup_action_list(cli: Group):

    @cli.command("list")
    @click.pass_context
    def list_logs(ctx, **kwargs):
        """List long entries (default)"""

        config = RunningConfigList(**kwargs)

        action_list(config)

    add_shared_arguments(list_logs)

__all__ = ("setup_action_list", )
