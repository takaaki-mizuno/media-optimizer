from ..base_process import BaseProcess
from pathlib import Path


class Zopflipng(BaseProcess):
    _command_name = "zopflipng"
    _save_to_same_file = False

    def get_options(self, input_path: Path, output_path: Path):
        return "{} {}".format(str(input_path.absolute()), str(output_path.absolute()))
