from pathlib import Path
from logging import Logger
from ..processes import BaseProcess
from typing import Type, Dict
import shutil


class BaseOptimizer(object):
    _preprocesses: [Type[BaseProcess]] = []
    _processes: [Type[BaseProcess]] = []
    _supported_suffix = []

    def __init__(self, temporary_directory: Path, logger: Logger, debug_mode: bool = False):
        self._temp_directory = temporary_directory
        self._logger = logger
        self._debug_mode = debug_mode
        self._available_preprocesses: [BaseProcess] = []
        self._available_processes: [BaseProcess] = []
        self.check_command_status()

    def supported_file(self, path: Path):
        return path.suffix in self._supported_suffix

    def check_command_status(self) -> Dict:
        result = {}
        for command in self._processes:
            instance = command(temporary_directory=self._temp_directory, logger=self._logger)
            exists = instance.exists()
            result[instance.command_name] = exists
            self._available_processes.append(instance)

        for command in self._preprocesses:
            instance = command(temporary_directory=self._temp_directory, logger=self._logger)
            exists = instance.exists()
            result[instance.command_name] = exists
            self._available_preprocesses.append(instance)

        return result

    def execute(self, source_file: Path, destination_file: Path) -> bool:
        if self.can_skip(source_file):
            self._logger.info("Skip {} ...".format(str(source_file.absolute())))
            return True
        self._logger.info("Start processing {} ...".format(str(source_file.absolute())))
        original_size = source_file.stat().st_size
        file = self.preprocess(source_file)
        smallest_file, composer = self.process(file)
        optimized_size = smallest_file.stat().st_size
        self._logger.info("{} -> {} : {} % By {} ".format(
            original_size, optimized_size, optimized_size / original_size, composer))
        if str(smallest_file.absolute()) != str(destination_file.absolute()):
            shutil.copy(smallest_file, destination_file)
        return True

    def can_skip(self, source_file: Path) -> bool:
        return False

    def preprocess(self, source_file: Path) -> Path:
        file = source_file
        for process in self._available_preprocesses:
            result_file = process.process(file)
            if result_file is not None:
                file = result_file
        return file

    def process(self, source_file: Path) -> (Path, str):
        file = source_file
        size = file.stat().st_size
        smallest_file = file
        smallest_file_composer = "None"
        for process in self._available_processes:
            result_file = process.process(file)
            if result_file is not None and result_file.exists():
                new_size = result_file.stat().st_size
                if new_size < size:
                    smallest_file = result_file
                    smallest_file_composer = process.command_name
        return smallest_file, smallest_file_composer
