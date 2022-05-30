import os
import sys
import json
import textwrap

from datetime import datetime

import click
import tabulate

from powerful_pipes_log_viewer import get_file_content_reports, LOG_LEVELS, \
    LOG_LEVELS_NAMES

from .models import RunningConfigShow

def wrap(
        text: str, width: int, color: str = None, center: bool = False
) -> str:
    if not text:
        return ""

    if center:
        return "\n".join([
            click.style(x.center(width), fg=color)
            if color else x.center(width)

            for x in
            textwrap.wrap(text, width=width)
        ])

    else:
        return "\n".join(textwrap.wrap(text, width=width))

def wrap_ln(
        text: str, width: int, color: str = None, center: bool = False
) -> str:
    if not text:
        return ""

    total_lines = []

    for ln in text.splitlines():
        line = ln.strip()

        if len(line) > width:

            if center:
                total_lines.extend(
                    x.center(width)
                    for x in
                    textwrap.wrap(line, width=width)
                )
            else:
                total_lines.extend(textwrap.wrap(line, width=width))

        else:

            if center:
                total_lines.append(line.center(width))
            else:
                total_lines.append(line)

    # Write lines
    return "\n".join(
        click.style(x, fg=color) if color else x
        for x in total_lines
    )

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
            ("Command Line", wrap(
                report.commandLine,
                width=second_column_width,
                color="magenta"
            )),
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
                data.append((
                    "Extra data",
                    wrap(str(report.data), second_column_width)
                ))

        if report.is_exception:
            data.append(("Exception", report.exceptionName))
            data.append(("Exception Message", report.exceptionMessage))
            data.append(("Exception file", report.binary))
            data.append((
                "Stack Trace",
                wrap_ln(report.stackTrace,
                        width=second_column_width,
                        color="red")
            ))
            data.append((
                wrap("Exception User Message", 15, center=True),
                wrap(report.userException, second_column_width)
            ))


        click.echo(tabulate.tabulate(data, tablefmt="grid"), file=sys.stderr)
        click.echo("\n", file=sys.stderr)

__all__ = ("action_show", )
