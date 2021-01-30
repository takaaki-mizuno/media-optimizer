from .base_optimizer import BaseOptimizer
from ..processes.jpeg import BaseProcess, optimizers
from typing import Type


class JpegOptimizer(BaseOptimizer):
    _preprocesses: [Type[BaseProcess]] = []
    _processes: [Type[BaseProcess]] = optimizers
    _supported_suffix = [".jpeg", ".jpg"]
