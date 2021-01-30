from ..base_process import BaseProcess
from pathlib import Path


class Pngcrush(BaseProcess):
    _command_name = "pngcrush"

    def get_options(self, input_path: Path, output_path: Path):
        return "-brute -q {} {}".format(str(input_path.absolute()), str(output_path.absolute()))
