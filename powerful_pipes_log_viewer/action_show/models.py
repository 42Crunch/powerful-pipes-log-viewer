from dataclasses import dataclass

from powerful_pipes_log_viewer import RunningConfig

@dataclass
class RunningConfigShow(RunningConfig):
    log_entry: int = None
