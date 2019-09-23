# -*- coding: utf-8 -*-

"""Tests for the LetterOccurances Statistics Generator module"""

from typing import List
import unittest

from text_statistics import LetterOccurances
from .base_stats_generator_test import BaseStatsGeneratorTest
from .unit_test_data import UnitTestData


class TestLetterOccurances(BaseStatsGeneratorTest, unittest.TestCase):
    """Test the LetterOccurances plugin using the python unittest framework."""

    @property
    def stats_generator_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects for BaseStatsGeneratorTest to test.
        """
        return [
            UnitTestData('No Letters', [''], expected_result=dict()),
            UnitTestData(
                'Multiple Letters',
                ['aa bc'],
                expected_result={'a': 2, 'b': 1, 'c': 1}
            ),
            UnitTestData(
                'Ignores Case',
                ['aa bBb C'],
                expected_result={'a': 2, 'b': 3, 'c': 1}
            ),
            UnitTestData(
                'Ignores Symbols',
                ['A!'],
                expected_result={'a': 1}
            ),
            UnitTestData(
                'Ignores Numbers',
                ["A123"],
                expected_result={'a': 1}
            ),
            UnitTestData(
                'Diacritical Marks',
                ["èe"],
                expected_result={'è': 1, 'e': 1}
            ),
            UnitTestData(
                'Multiple Lines',
                [
                    'a\n',
                    'b',
                ],
                expected_result={'a': 1, 'b': 1}
            ),
            UnitTestData(
                'Non-Latin Charset',
                ['你好'],
                expected_result={'你': 1, '好': 1}
            ),
        ]

    @staticmethod
    def get_stats_generator() -> LetterOccurances:
        """Return a new LetterOccurances object."""
        return LetterOccurances()
