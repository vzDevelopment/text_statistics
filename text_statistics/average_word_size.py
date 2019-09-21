# -*- coding: utf-8 -*-

from .letter_count import LetterCount
from .statistics_generator import StatisticsGenerator
from .word_count import WordCount


class AverageWordSize(StatisticsGenerator):
    def __init__(self, decimal_places=1):
        super().__init__('Average Word Size')

        self._decimal_places = decimal_places

        self._word_count = WordCount()
        self._letter_count = LetterCount()

    def parse_line(self, line):
        self._word_count.parse_line(line)
        self._letter_count.parse_line(line)

    def result(self):
        try:
            # We're using Python3 so this will use true division
            result = self._letter_count.result() / self._word_count.result()
        except ZeroDivisionError:
            result = 0

        return round(result, self._decimal_places)
