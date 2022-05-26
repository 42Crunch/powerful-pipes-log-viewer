import sys

import click

from powerful_pipes_log_viewer import get_file_content_reports, LOG_LEVELS, LOG_LEVELS_NAMES

from .models import RunningConfigList

def action_list(config: RunningConfigList):

    for index, (binary, report) in enumerate(
            get_file_content_reports(
                config.log_file,
                enable_stream=config.stream
            ), start=1
    ):
        if config.only_exceptions and not report.is_exception:
            continue

        # Specific log level
        if config.log_level:
            log_level = LOG_LEVELS[config.log_level]

            if report.logLevel < log_level:
                continue

        custom_message = ""

        if report.is_exception:
            custom_message = report.exceptionMessage

        elif report.message:
            custom_message = report.message

        elif report.data:
            custom_message = str(report.data)

        fg_color = "red" if report.is_exception else "blue"

        if report.is_exception:
            message_exception_or_log = click.style("Exception".center(9), fg=fg_color)
        else:

            message_exception_or_log = click.style(
                LOG_LEVELS_NAMES[report.logLevel].center(9),
                fg=fg_color
            )

        msg_index = f"{index})"
        msg_msg = click.style(custom_message, fg=fg_color)
        msg_binary = click.style(binary, fg="white")

        message = f"{msg_index:4} [{message_exception_or_log}] {msg_binary} -> '{msg_msg}'"

        click.echo(message, file=sys.stderr)



__all__ = ("action_list", )
