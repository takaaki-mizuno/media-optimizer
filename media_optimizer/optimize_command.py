import logging
from pathlib import Path
from typing import Optional
from .optimizers import BaseOptimizer, PngOptimizer, Mp3Optimizer, JpegOptimizer
import tempfile
import shutil


class OptimizeCommand(object):
    def __init__(self, logger: Optional[logging.Logger] = None):
        if logger is None:
            self._logger = logging.getLogger("Optimizer")
        else:
            self._logger = logger
        logging.basicConfig(level=logging.INFO)
        self._logger.setLevel(logging.INFO)
        self._optimizers: [BaseOptimizer] = []

    def optimize(self, path: str):
        with tempfile.TemporaryDirectory() as temporary_directory_name:
            temporary_directory = Path(temporary_directory_name)
            self._optimizers = [
                PngOptimizer(temporary_directory=temporary_directory, logger=self._logger),
                JpegOptimizer(temporary_directory=temporary_directory, logger=self._logger),
                Mp3Optimizer(temporary_directory=temporary_directory, logger=self._logger),
            ]
            target_path = Path(path)
            if not target_path.exists():
                self._logger.error("Path %s Not Found" % target_path(path))
            if not target_path.is_dir():
                self._optimize_file(target_path)
            else:
                for file in target_path.glob('**/*'):
                    self._optimize_file(file)

    def _optimize_file(self, path: Path):
        for optimizer in self._optimizers:
            if optimizer.supported_file(path):
                optimizer.execute(path, path)
