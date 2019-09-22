# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Any


class StatisticsGenerator(ABC):
    def __init__(self, name: str) -> None:
        self._name: str = str(name)

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def parse_line(self, line: str) -> None:
        pass

    @abstractmethod
    def result(self) -> Any:
        pass

    def __str__(self) -> str:
        return "{}: {}".format(self.name, self.result())
