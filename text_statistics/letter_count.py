# -*- coding: utf-8 -*-

""" Provides a Statistics Generator Plugin to calculate the number of letters
    in a piece of text.
"""

from .statistics_generator import StatisticsGenerator


class LetterCount(StatisticsGenerator):
    """This class counts the number of alphanumeric characters that are parsed.

    Numbers are intentionally included so that average letter counts are
    accurate when text contains numeric words e.g. "10 apples".
    """
    def __init__(self) -> None:
        self._count: int = 0

    def parse_line(self, line: str) -> None:
        """Count the number of letters in the provided line."""
        for letter in line:
            if letter.isalnum():
                self._count += 1

    def result(self) -> int:
        """Return the number of letters seen."""
        return self._count
