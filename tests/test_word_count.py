# -*- coding: utf-8 -*-

"""Tests for the WordCount Statistics Generator module"""

import unittest

from text_statistics import WordCount
from .unit_test_data import UnitTestData


class TestWordCount(unittest.TestCase):
    """
    Attributes:
        tests: A list of UnitTestData objects containing test data and the
            expected result from the WordCount object once this data has
            been parsed.
    """
    def setUp(self):
        self.tests = [
            UnitTestData('No Words', [''], expected_result=0),
            UnitTestData('One Word', ['Hello'], expected_result=1),
            UnitTestData('One Line', ['Hello, World!'], expected_result=2),
            UnitTestData(
                'Multiple Lines',
                [
                    'This is the first line\n',
                    'And this is the second line',
                ],
                expected_result=11
            ),
            UnitTestData(
                'Multiple Whitespace',
                ['This  has inconsistent    whitespace'],
                expected_result=4
            ),
            UnitTestData(
                'Trailing Whitespace',
                [' Trailing whitespace  '],
                expected_result=2
            ),
            UnitTestData(
                'UTF-8 String',
                ['È in italiano'],
                expected_result=3
            ),
            UnitTestData(
                'Non-Latin Charset',
                ['它是中文的'],
                expected_result=1
            ),
        ]

    def test_word_count(self):
        """Test each entry in the tests fixture"""
        for test in self.tests:
            # Create a new WordCount object to erase the state from the
            # previous test
            word_count = WordCount()

            for line in test.lines:
                word_count.parse_line(line)

            actual_result = word_count.result()
            self.assertEqual(
                actual_result,
                test.expected_result,
                "'{}' test failed. Got: '{}' but expected: '{}'".format(
                    test.name, actual_result, test.expected_result
                )
            )
