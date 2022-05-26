import click

from click import Command

from .models import LOG_LEVELS


def add_shared_arguments(cli: Command):

    click.option(
        "-e", "--only-exceptions",
        is_flag=True,
        default=False,
        help="only display exception messages"
    )(cli)
    click.option(
        "-l", "--log-level",
        default=None,
        help="only display log level higher than specified",
        type=click.Choice(
            LOG_LEVELS.keys(),
            case_sensitive=False
        )
    )(cli)
    click.option(
        "--stream",
        default=False,
        is_flag=True,
        help="enable stream mode",
    )(cli)
    click.argument("log_file", nargs=-1)(cli)


__all__ = ("add_shared_arguments",)
