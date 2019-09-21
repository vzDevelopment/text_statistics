# -*- coding: utf-8 -*-

from .statistics_generator import StatisticsGenerator


class MostCommonLetter(StatisticsGenerator):
    def __init__(self):
        super().__init__('Most Common Letter')
        self._letters = {}

    # Although this doesn't currently use self, it's not static because we may
    # want to configure it in the future e.g. to take case or diacritical marks
    # into account
    def _normalise_letter(self, letter):
        return letter.lower()

    def parse_line(self, line):
        for letter in line:
            if not letter.isalpha():
                continue

            letter = self._normalise_letter(letter)

            if letter in self._letters:
                self._letters[letter] += 1
            else:
                self._letters[letter] = 1

    def result(self):
        if not self._letters:
            return set()

        max_value = max(self._letters.values())
        return {
            key for key in self._letters if self._letters[key] == max_value
        }
