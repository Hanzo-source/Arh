import os
from dataclasses import dataclass

from command import view_cmd


@dataclass
class ViewArhive:
    input_file: str

    def tar_view(self) -> None:
        os.system(f"{view_cmd.get('tar')} {self.input_file}")

    def zip_view(self) -> None:
        os.system(f"{view_cmd.get('zip')} {self.input_file}")

    def rar_view(self) -> None:
        os.system(f"{view_cmd.get('rar')} {self.input_file}")

    def sevenzip_view(self) -> None:
        os.system(f"{view_cmd.get('7z')} {self.input_file}")
