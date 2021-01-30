from ..base_process import BaseProcess
from .sox import Sox
from typing import List, Type

optimizers: List[Type[BaseProcess]] = [Sox]

processes: List[Type[BaseProcess]] = []
processes.extend(optimizers)

