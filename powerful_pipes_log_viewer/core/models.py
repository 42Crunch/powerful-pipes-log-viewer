from __future__ import annotations

from dataclasses import dataclass

from powerful_pipes import REPORT_LEVEL


@dataclass
class RunningConfig:
    log_file: str
    only_exceptions: bool = False
    log_level: int = None
    stream: bool = False

    def __post_init__(self):
        if self.log_file:
            self.log_file = self.log_file[0]
        else:
            self.log_file = "-"


@dataclass
class Report:
    logLevel: int
    commandLine: str
    epoch: float

    # Exception fields
    is_exception: bool = False
    exceptionName: str = None
    exceptionMessage: str = None
    binary: str = None
    stackTrace: str = None

    # Custom exception fields
    userException: str = None

    # Custom user messages
    message: str = None
    data: object = None

    @classmethod
    def from_powerful_pipes_report(cls, report: dict) -> Report:

        common = dict(
            logLevel=report.get("logLevel"),
            commandLine=report.get("commandLine"),
            epoch=report.get("epoch")
        )

        if ex := report.get("exceptionDetails", None):
            common.update({
                "is_exception": True,
                "exceptionName": ex.get("exceptionName"),
                "exceptionMessage": ex.get("exceptionMessage"),
                "binary": ex.get("binary"),
                "stackTrace": ex.get("stackTrace")
            })

            if user_exc := ex.get("userException"):
                common["userException"] = user_exc

        if message := report.get("message", None):
            common["message"] = message

        if data := report.get("data", None):
            common["data"] = data

        return cls(**common)


LOG_LEVELS = {x: v for x, v in REPORT_LEVEL.__dict__.items() if not x.startswith("_")}
LOG_LEVELS_NAMES = {v: x for x, v in REPORT_LEVEL.__dict__.items() if not x.startswith("_")}
