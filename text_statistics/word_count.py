# -*- coding: utf-8 -*-

from .statistics_generator import StatisticsGenerator


class WordCount(StatisticsGenerator):
    def __init__(self):
        super().__init__('Word Count')
        self._word_count = 0

    def parse_line(self, line):
        words_in_line = len(line.split())
        self._word_count += words_in_line

    def result(self):
        return self._word_count
