from .base_optimizer import BaseOptimizer
from ..processes.mp3 import BaseProcess, optimizers
from typing import Type
from pathlib import Path
from mutagen.mp3 import MP3


class Mp3Optimizer(BaseOptimizer):
    _preprocesses: [Type[BaseProcess]] = []
    _processes: [Type[BaseProcess]] = optimizers
    _supported_suffix = [".mp3"]

    def can_skip(self, source_file: Path) -> bool:
        mp3file = MP3(str(source_file))
        bitrate = mp3file.info.bitrate / 1000
        if bitrate <= 64.0:
            return True
        return False
