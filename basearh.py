import os
from dataclasses import dataclass


@dataclass
class BaseArh:
    input_file: str
    output_name: str
    silent_mode: str

    def __post_init__(self):
        self.create_output_dir = (
            "" if os.path.isdir(self.output_name) else f"mkdir {self.output_name} &&"
        )

        self.silent = ">/dev/null" if self.silent_mode else ""
