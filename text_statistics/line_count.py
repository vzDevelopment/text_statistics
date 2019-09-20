# -*- coding: utf-8 -*-

from .statistics_generator import StatisticsGenerator


class LineCount(StatisticsGenerator):
    def __init__(self):
        super().__init__('Line Count')
        self._count = 0

    def parse_line(self, line):
        self._count += 1

    def result(self):
        return self._count
