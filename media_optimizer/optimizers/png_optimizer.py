from .base_optimizer import BaseOptimizer
from ..processes.png import BaseProcess, Pngquant, optimizers
from typing import Type
from pathlib import Path


class PngOptimizer(BaseOptimizer):
    _preprocesses: [Type[BaseProcess]] = [Pngquant]
    _processes: [Type[BaseProcess]] = optimizers
    _supported_suffix = [".png"]

    def can_skip(self, source_file: Path) -> bool:
        return False
