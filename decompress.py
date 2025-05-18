import os

from basearh import BaseArh
from command import decompress_cmd


class Decompress(BaseArh):
    def tar_decompress(self) -> None:
        os.system(
            f"{self.create_output_dir} {decompress_cmd.get('tar')} {self.input_file} -C {self.output_name} {self.silent}"
        )

    def tar_bz2_decompress(self) -> None:
        os.system(
            f"{self.create_output_dir} {decompress_cmd.get('tar_bz2')} {self.input_file} -C {self.output_name} {self.silent}"
        )

    def tar_gz_decompress(self) -> None:
        os.system(
            f"{self.create_output_dir} {decompress_cmd.get('tar_gz')} {self.input_file} -C {self.output_name} {self.silent}"
        )

    def tar_xz_decompress(self) -> None:
        os.system(
            f"{self.create_output_dir} {decompress_cmd.get('tar_xz')} {self.input_file} -C '{self.output_name}' {self.silent}"
        )

    def zip_decompress(self) -> None:
        os.system(
            f"{self.create_output_dir} {decompress_cmd.get('zip')} {self.output_name} {self.input_file} {self.silent}"
        )

    def rar_decompress(self) -> None:
        os.system(
            f"{self.create_output_dir} {decompress_cmd.get('rar')} {self.input_file} {self.output_name} {self.silent}"
        )

    def sevenzip_decompress(self) -> None:
        os.system(
            f"{self.create_output_dir} {decompress_cmd.get('sevenzip')} {self.input_file} -o{self.output_name} {self.silent}"
        )
