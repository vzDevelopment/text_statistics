# -*- coding: utf-8 -*-

""" Provide a Statistics Generator Plugin which can be used to calculate the
    average word size to a given precision.

    This module is designed to be used with the TextStatistics class.
"""

from .letter_count import LetterCount
from .statistics_generator import StatisticsGenerator
from .word_count import WordCount


class AverageWordSize(StatisticsGenerator):
    """This class calculates the average word size for the parsed strings."""

    def __init__(self, decimal_places: int = 1) -> None:
        """Initialise the AverageWordSize object

        Arguments:
            decimal_places: the number of decimal places to use for the result
        """
        self._decimal_places: int = decimal_places

        self._word_count: WordCount = WordCount()
        self._letter_count: LetterCount = LetterCount()

    def parse_line(self, line: str) -> None:
        """Parse the provided line and add it to the stats.

        Arguments:
            line: a line of text to process
        """
        self._word_count.parse_line(line)
        self._letter_count.parse_line(line)

    def result(self) -> float:
        """Return the average word size for the lines parsed by the object.

        The precision is based on the number of decimal places configured in
        the object.
        """
        result: float
        try:
            # We're using Python3 so this will use true division
            result = self._letter_count.result() / self._word_count.result()
        except ZeroDivisionError:
            result = 0

        return round(result, self._decimal_places)
