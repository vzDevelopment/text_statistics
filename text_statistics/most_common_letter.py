# -*- coding: utf-8 -*-

""" Provides a Statistics Generator Plugin to calculate the most common letters
    in a piece of text.
"""

from typing import Dict, Set

from .statistics_generator import StatisticsGenerator


class MostCommonLetter(StatisticsGenerator):
    """This class keeps track of the most commonly used letters.

    It is case in-sensitive, but treats accented letters as different e.g. "è"
    is considered to be a different letter to "e".

    This class considers only alphabetical characters (those returned by
    str.isalpha()) to be a letter.
    """

    def __init__(self) -> None:
        self._letters: Dict[str, int] = {}

    # Although this doesn't currently use self, it's not static because we may
    # want to configure it in the future e.g. to take case or diacritical marks
    # into account
    def _normalise_letter(self, letter: str) -> str:
        """Convert the letter to a standard form.

        This allows us to decide which letters should be treated equally. E.g.
        we want the statistics to be case in-sensitive so return the lower-
        cased version.

        Arguments:
            letter: the letter to normalise

        Return: a normalised letter
        """
        return letter.lower()

    def parse_line(self, line: str) -> None:
        """Count the number of occurances per letter in the provided line."""
        for letter in line:
            if not letter.isalpha():
                continue

            # Decide how we should count this letter e.g. if "A" == "a"
            letter = self._normalise_letter(letter)

            if letter in self._letters:
                self._letters[letter] += 1
            else:
                self._letters[letter] = 1

    def result(self) -> Set[str]:
        """Return a set containing the most common letters seen."""
        if not self._letters:
            return set()

        # There may be more than one letter which occurs the most times, so
        # return a set containing all of them
        max_value: int = max(self._letters.values())
        return {
            key for key in self._letters if self._letters[key] == max_value
        }
