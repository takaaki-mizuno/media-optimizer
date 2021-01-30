from ..base_process import BaseProcess
from pathlib import Path


class Optipng(BaseProcess):
    _command_name = "optipng"

    def get_options(self, input_path: Path, output_path: Path):
        return "-out {} -o7 {}".format(str(output_path.absolute()), str(input_path.absolute()))
