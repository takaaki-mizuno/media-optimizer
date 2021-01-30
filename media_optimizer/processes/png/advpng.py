from ..base_process import BaseProcess
from pathlib import Path


class Advpng(BaseProcess):
    _command_name = "advpng"
    _save_to_same_file = True

    def get_options(self, input_path: Path, output_path: Path):
        return "-z -4 {}".format(str(output_path.absolute()))
