# -*- coding: utf-8 -*-

""" Provides a Statistics Generator Plugin to calculate the most common letters
    in a piece of text.
"""

from typing import Set

from .letter_occurances import LetterOccurances
from .statistics_generator import StatisticsGenerator


class MostCommonLetter(StatisticsGenerator):
    """This class keeps track of the most commonly used letters.

    It is case in-sensitive, but treats accented letters as different e.g. "è"
    is considered to be a different letter to "e".

    This class considers only alphabetical characters (those returned by
    str.isalpha()) to be a letter.
    """
    def __init__(self) -> None:
        self._letter_occurance = LetterOccurances()

    def parse_line(self, line: str) -> None:
        """Track the number of occurances per letter in the provided line."""
        self._letter_occurance.parse_line(line)

    def result(self) -> Set[str]:
        """Return a set containing the most common letters seen."""
        letters = self._letter_occurance.result()

        if not letters:
            return set()

        # There may be more than one letter which occurs the most times, so
        # return a set containing all of them
        max_value: int = max(letters.values())
        return {
            key for key in letters if letters[key] == max_value
        }
