from ..base_process import BaseProcess
from pathlib import Path
from PIL import Image


class Pngquant(BaseProcess):
    _command_name = "pngquant"
    _save_to_same_file = False

    def get_options(self, input_path: Path, output_path: Path):
        return "--force --output {} --speed 1 256 {}".format(str(output_path.absolute()), str(input_path.absolute()))

    def can_skip(self, source_file: Path) -> bool:
        image = Image.open(source_file)
        if image.mode == "P":
            return True
        self._logger.info("Mode: {}".format(image.mode))
        return False
