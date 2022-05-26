import click

from click import Context

def action_help(ctx: Context):
    ct = click.get_current_context()
    click.echo(ct.get_help())


__all__ = ("action_help", )
