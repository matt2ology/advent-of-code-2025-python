# base_day.py
import logging

FORMAT = '[%(asctime)s]-[%(funcName)s]-[%(levelname)s] - %(message)s'

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT
)


class BaseDay:
    def __init__(self, data: list[str]):
        self.data = data
        # Create a logger named after the current class (e.g., "Day01")
        self.logging = logging.getLogger(self.__class__.__name__)
