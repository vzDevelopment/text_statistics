# -*- coding: utf-8 -*-

from .statistics_generator import StatisticsGenerator


class LetterCount(StatisticsGenerator):
    def __init__(self) -> None:
        self._count: int = 0

    def parse_line(self, line: str) -> None:
        for letter in line:
            if letter.isalnum():
                self._count += 1

    def result(self) -> int:
        return self._count
