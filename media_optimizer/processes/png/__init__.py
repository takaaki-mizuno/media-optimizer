from ..base_process import BaseProcess
from .pngcrush import Pngcrush
from .advpng import Advpng
from .optipng import Optipng
from .zopflipng import Zopflipng
from .pngquant import Pngquant
from typing import List, Type

optimizers: List[Type[BaseProcess]] = [Zopflipng]

processes: List[Type[BaseProcess]] = [Pngquant]
processes.extend(optimizers)
