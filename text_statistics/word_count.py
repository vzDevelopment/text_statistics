# -*- coding: utf-8 -*-

""" Provides a Statistics Generator Plygin to calculate the number of words
    in text.
"""

from .statistics_generator import StatisticsGenerator


class WordCount(StatisticsGenerator):
    """This class counts the number of words that are parsed.

    A word is defined as anything delimited by whitespace.
    """
    def __init__(self) -> None:
        self._word_count: int = 0

    def parse_line(self, line: str) -> None:
        """Count the number of words in the provided line."""
        words_in_line: int = len(line.split())
        self._word_count += words_in_line

    def result(self) -> int:
        """Return the number of words seen."""
        return self._word_count
