from ..base_process import BaseProcess
from pathlib import Path


class Jpegtran(BaseProcess):
    _command_name = "jpegtran"
    _save_to_same_file = False

    def get_options(self, input_path: Path, output_path: Path):
        return " -optimize -trim -outfile {} {}".format(str(output_path.absolute()), str(input_path.absolute()))
