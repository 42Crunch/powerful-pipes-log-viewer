import json
import os
import sys
import textwrap
from datetime import datetime

import click
import tabulate
from powerful_pipes import read_json

from powerful_pipes_log_viewer import get_file_content_reports, LOG_LEVELS, LOG_LEVELS_NAMES

from .models import RunningConfigShow

def wrap(text: str, width: int, center: bool = False) -> str:
    if center:
        return "\n".join([
          x.center(width)
          for x in
          textwrap.wrap(text, width=width)
        ])

    else:
        return "\n".join(textwrap.wrap(text, width=width))

def action_show(config: RunningConfigShow):

    try:
        terminal_size = os.get_terminal_size().columns
    except OSError:
        terminal_size = 72

    first_column_width = 25
    second_column_width = terminal_size - first_column_width - 5

    for index, (binary, report) in enumerate(
            get_file_content_reports(
                config.log_file,
                enable_stream=config.stream
            ), start=1
    ):
        if config.log_entry and config.log_entry != index:
            continue

        if config.only_exceptions and not report.is_exception:
            continue

        # Specific log level
        if config.log_level:
            log_level = LOG_LEVELS[config.log_level]

            if report.logLevel < log_level:
                continue

        fg_color = "red" if report.is_exception else "green"

        data = [
            ("Number", index),
            ("Command Line", click.style(wrap(report.commandLine, width=second_column_width), fg="magenta")),
            ("Date", datetime.fromtimestamp(report.epoch) ),
        ]

        if report.is_exception:
            message_exception_or_log = click.style(
                "Exception",
                fg=fg_color
            )
        else:

            message_exception_or_log = click.style(
                LOG_LEVELS_NAMES[report.logLevel],
                fg=fg_color
            )

        data.append(("Type", message_exception_or_log))

        if report.message:
            data.append(("Message", wrap(report.message, second_column_width)))

        if report.data:

            try:
                pretty_json = json.dumps(
                    report.data, indent=4, sort_keys=True
                )
                data.append(("Extra data", pretty_json))
            except:
                data.append(("Extra data", wrap(str(report.data), second_column_width)))

        if report.is_exception:
            data.append(("Exception", report.exceptionName))
            data.append(("Exception Message", report.exceptionMessage))
            data.append(("Exception file", report.binary))
            data.append(("Stack Trace", click.style(report.stackTrace, fg="red")))
            data.append((
                wrap("Exception User Message", 15, center=True),
                wrap(report.userException, second_column_width)
            ))


        click.echo(tabulate.tabulate(data, tablefmt="grid"), file=sys.stderr)
        click.echo("\n", file=sys.stderr)

__all__ = ("action_show", )
