# -*- coding: utf-8 -*-

from .statistics_generator import StatisticsGenerator


class LetterCount(StatisticsGenerator):
    def __init__(self):
        super().__init__('Letter Count')
        self._count = 0

    def parse_line(self, line):
        for letter in line:
            if letter.isalnum():
                self._count += 1

    def result(self):
        return self._count
