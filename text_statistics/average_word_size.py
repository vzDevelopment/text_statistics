# -*- coding: utf-8 -*-

from .letter_count import LetterCount
from .statistics_generator import StatisticsGenerator
from .word_count import WordCount


class AverageWordSize(StatisticsGenerator):
    def __init__(self, decimal_places: int = 1) -> None:
        self._decimal_places: int = decimal_places

        self._word_count: WordCount = WordCount()
        self._letter_count: LetterCount = LetterCount()

    def parse_line(self, line: str) -> None:
        self._word_count.parse_line(line)
        self._letter_count.parse_line(line)

    def result(self) -> float:
        result: float
        try:
            # We're using Python3 so this will use true division
            result = self._letter_count.result() / self._word_count.result()
        except ZeroDivisionError:
            result = 0

        return round(result, self._decimal_places)
