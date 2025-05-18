import os

from basearh import BaseArh
from command import compress_cmd


class Compress(BaseArh):
    def tar_compress(self) -> None:
        os.system(
            f"{compress_cmd.get('tar')} {self.output_name + ".tar"} {self.input_file} {self.silent}"
        )

    def tar_bz2_compress(self) -> None:
        os.system(
            f"{compress_cmd.get('tar_bz2')} {self.output_name + ".tar.bz2"} {self.input_file} {self.silent}"
        )

    def tar_gz_compress(self) -> None:
        os.system(
            f"{compress_cmd.get('tar_gz')} {self.output_name + ".tar.gz"} {self.input_file} {self.silent}"
        )

    def tar_xz_compress(self) -> None:
        os.system(
            f"{compress_cmd.get('tar_xz')} {self.output_name + ".tar.xz"} {self.input_file} {self.silent}"
        )

    def zip_compress(self) -> None:
        cmd = f"{self.output_name} {self.input_file}"

        if os.path.isfile(self.input_file):
            os.system(f"{compress_cmd.get('zip')} {cmd} {self.silent}")

        else:
            os.system(f"{compress_cmd.get('zip_dir')} {cmd} {self.silent}")

    def rar_compress(self) -> None:
        os.system(
            f"{compress_cmd.get('rar')} {self.output_name + ".rar"} {self.input_file} {self.silent}"
        )

    def sevenzip_compress(self) -> None:
        os.system(
            f"{compress_cmd.get('sevenzip')} {self.output_name + ".7z"} {self.input_file} {self.silent}"
        )
