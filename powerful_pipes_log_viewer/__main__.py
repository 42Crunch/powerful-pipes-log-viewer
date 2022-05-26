import sys

import click

from powerful_pipes_log_viewer.action_list import setup_action_list
from powerful_pipes_log_viewer.action_help import setup_action_help
from powerful_pipes_log_viewer.action_show import setup_action_show


@click.group()
@click.pass_context
def cli(ctx):
    ...

setup_action_list(cli)
setup_action_show(cli)
setup_action_help(cli)

def main():

    try:
        cli()
    except Exception as e:
        click.echo(f"[!] Error: {e}")

if __name__ == '__main__':
    main()
