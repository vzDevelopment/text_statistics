# -*- coding: utf-8 -*-

"""Tests for the LineCount Statistics Generator module"""

import unittest

from text_statistics import LineCount
from .unit_test_data import UnitTestData


class TestLineCount(unittest.TestCase):
    """
    Attributes:
        tests: A list of UnitTestData objects containing test data and the
            expected result from the LineCount object once this data has
            been parsed.
    """
    def setUp(self):
        self.tests = [
            UnitTestData('No Lines', [], expected_result=0),
            UnitTestData('One Line', ['Hello'], expected_result=1),
            UnitTestData(
                'One Line with trailing newline',
                ['Hello\n'],
                expected_result=1
            ),
            UnitTestData(
                'Multiple Lines',
                [
                    'Line1\n',
                    'Line2\n',
                ],
                expected_result=2
            ),
        ]

    def test_line_count(self):
        """Test each entry in the tests fixture"""
        for test in self.tests:
            # Create a new object to erase the state from the
            # previous test
            line_count = LineCount()

            for line in test.lines:
                line_count.parse_line(line)

            actual_result = line_count.result()
            self.assertEqual(
                actual_result,
                test.expected_result,
                "'{}' test failed. Got: '{}' but expected: '{}'".format(
                    test.name, actual_result, test.expected_result
                )
            )
