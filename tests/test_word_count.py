# -*- coding: utf-8 -*-

import unittest

from text_statistics import WordCount


class TestWordCount(unittest.TestCase):
    def setUp(self):
        self.word_count = WordCount()
        # TODO add fixture to remove duplication

    def test_no_words(self):
        line = ''
        self.word_count.parse_line(line)
        self.assertEqual(self.word_count.result(), 0)

    def test_one_word(self):
        line = 'Hello'
        self.word_count.parse_line(line)
        self.assertEqual(self.word_count.result(), 1)

    def test_one_line(self):
        line = 'Hello, World!'
        self.word_count.parse_line(line)
        self.assertEqual(self.word_count.result(), 2)

    def test_multiple_lines(self):
        lines = [
                'This is the first line',
                'And this is the second line',
        ]

        for line in lines:
            self.word_count.parse_line(line)

        self.assertEqual(self.word_count.result(), 11)

    def test_multiple_whitespace(self):
        line = 'This  has inconsistent    whitespace'
        self.word_count.parse_line(line)
        self.assertEqual(self.word_count.result(), 4)

    def test_trailing_space(self):
        line = ' Trailing whitespace  '
        self.word_count.parse_line(line)
        self.assertEqual(self.word_count.result(), 2)

    def test_utf8(self):
        line = 'È in italiano'
        self.word_count.parse_line(line)
        self.assertEqual(self.word_count.result(), 3)

    def test_non_latin_charset(self):
        line = '它是中文的'
        self.word_count.parse_line(line)
        self.assertEqual(self.word_count.result(), 1)
