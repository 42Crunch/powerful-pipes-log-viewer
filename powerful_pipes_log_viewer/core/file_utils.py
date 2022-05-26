from powerful_pipes import read_json, read_json_from_stdin, write_json_to_stdout

from typing import Iterable, Tuple

from .models import Report


def _get_from_stdin_() -> Iterable[dict]:
    for error, json_info in read_json_from_stdin():
        if error:
            continue

        yield json_info

def _get_from_file_(file_name: str) -> Iterable[dict]:

    with open(file_name, "r") as f:
        for line in f.readlines():

            try:
                yield read_json(line)
            except:
                continue

def get_file_content_reports(
        file_name: str,
        enable_stream: bool = False
) -> Iterable[Tuple[str, Report]] or None:
    if not file_name:
        return None

    if type(file_name) in (tuple, list):
        file_name = file_name[0]

    if file_name in ("-", ""):
        gen = _get_from_stdin_()

    else:
        gen =  _get_from_file_(file_name)

    for json_content in gen:

        if not (meta := json_content.get("_meta")):

            if enable_stream:
                write_json_to_stdout(json_content)

            continue

        if type(meta) is not dict:
            if enable_stream:
                write_json_to_stdout(json_content)

            continue

        if reports := meta.get("reporting"):

            for binary, report in reports.items():
                try:
                    yield binary, Report.from_powerful_pipes_report(report)
                except Exception as e:
                    print(e)

        if enable_stream:
            write_json_to_stdout(json_content)

__all__ = ("get_file_content_reports",)
