# -*- coding: utf-8 -*-

from .statistics_generator import StatisticsGenerator


class WordCount(StatisticsGenerator):
    def __init__(self) -> None:
        super().__init__('Word Count')
        self._word_count: int = 0

    def parse_line(self, line: str) -> None:
        words_in_line: int = len(line.split())
        self._word_count += words_in_line

    def result(self) -> int:
        return self._word_count
