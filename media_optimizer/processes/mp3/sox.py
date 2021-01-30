# sox source.mp3 -r 64000 -c 1 result.mp3
from ..base_process import BaseProcess
from pathlib import Path


class Sox(BaseProcess):
    _command_name = "sox"
    _save_to_same_file = False

    def get_options(self, input_path: Path, output_path: Path):
        return "{} -r 64000 -c 1 {}".format(str(input_path.absolute()), str(output_path.absolute()))
