# -*- coding: utf-8 -*-

""" Provides a Statistics Generator Plugin to track the number of times letters
    occur.
"""

from typing import Dict

from .statistics_generator import StatisticsGenerator


class LetterOccurances(StatisticsGenerator):
    """This class keeps track of how often letters occur.

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
    def _normalise_letter(self, letter: str) -> str:  # pylint: disable=no-self-use
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

    def result(self) -> Dict[str, int]:
        """Return a dictionary containing the number of times letters occur."""
        return self._letters
