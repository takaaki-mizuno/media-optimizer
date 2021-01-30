from pathlib import Path
import shutil
from typing import Optional
import time
from media_optimizer.utilities import Strings
from logging import Logger
import subprocess


class BaseProcess(object):
    _command_name = ""
    _params = ""
    _save_to_same_file = False

    @property
    def command_name(self):
        return self._command_name

    def __init__(self, temporary_directory: Path, logger: Logger, debug_mode: bool = False):
        self._temp_directory = temporary_directory
        self._logger = logger
        self._debug_mode = debug_mode

    def get_options(self, input_path: Path, output_path: Path):
        raise NotImplemented

    def exists(self) -> Optional[str]:
        return shutil.which(self._command_name)

    def can_skip(self, source_file: Path) -> bool:
        return False

    def process(self, path: Path) -> Optional[Path]:
        if self.can_skip(path):
            return path

        temp_file = self._temp_directory.joinpath(self._get_temp_file_name(path.suffix))
        if self._debug_mode:
            self._logger.debug("{}: Output path: {}", self._command_name, str(temp_file))
        command = self._command_name + " " + self.get_options(path, temp_file)
        if self._save_to_same_file:
            shutil.copy(path, temp_file)

        result = subprocess.run(command.split(" "), capture_output=True)
        if result.returncode != 0:
            if self._debug_mode:
                self._logger.warning(
                    "File {} with command {} generate error: {}".format(str(path.absolute()), self._command_name,
                                                                        result.stdout))
            return None
        return temp_file

    def _get_temp_file_name(self, extension: str) -> str:
        return self._command_name + str(time.time()) + Strings().random_string(10) + extension
