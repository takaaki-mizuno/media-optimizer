from ..base_process import BaseProcess
from .jpegtran import Jpegtran
from typing import List, Type

optimizers: List[Type[BaseProcess]] = [Jpegtran]

processes: List[Type[BaseProcess]] = []
processes.extend(optimizers)
