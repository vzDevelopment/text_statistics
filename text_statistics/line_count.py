# -*- coding: utf-8 -*-

""" Provides a Statistics Generator Plugin to calculate the number of lines
    in a piece of text.
"""

from .statistics_generator import StatisticsGenerator


class LineCount(StatisticsGenerator):
    """This class keeps track of the number of lines seen in a text file."""

    def __init__(self) -> None:
        self._count: int = 0

    def parse_line(self, line: str) -> None:
        """Parse a line from the text file."""
        self._count += 1

    def result(self) -> int:
        """Return the number of lines seen in the text file."""
        return self._count
