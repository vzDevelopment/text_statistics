# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Any


class StatisticsGenerator(ABC):
    @abstractmethod
    def parse_line(self, line: str) -> None:
        pass

    @abstractmethod
    def result(self) -> Any:
        pass

    def __str__(self) -> str:
        return f"{self.result()}"
