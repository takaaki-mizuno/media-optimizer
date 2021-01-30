import logging
from pathlib import Path
from typing import Optional
from .processes.png import processes as png_processes
from .processes.jpeg import processes as jpeg_processes
from .processes.mp3 import processes as mp3_processes


class StatusCommand(object):
    def __init__(self, logger: Optional[logging.Logger] = None):
        if logger is None:
            self._logger = logging.getLogger("Optimizer")
        else:
            self._logger = logger

    def get_status(self):
        for process in png_processes:
            process_instance = process(Path("/"), self._logger)
            exist = process_instance.exists()
            if exist:
                print("{}: Exists".format(process_instance.command_name))
            else:
                print("{}: Not Exists".format(process_instance.command_name))

        for process in jpeg_processes:
            process_instance = process(Path("/"), self._logger)
            exist = process_instance.exists()
            if exist:
                print("{}: Exists".format(process_instance.command_name))
            else:
                print("{}: Not Exists".format(process_instance.command_name))

        for process in mp3_processes:
            process_instance = process(Path("/"), self._logger)
            exist = process_instance.exists()
            if exist:
                print("{}: Exists".format(process_instance.command_name))
            else:
                print("{}: Not Exists".format(process_instance.command_name))
