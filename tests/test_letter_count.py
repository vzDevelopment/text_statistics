# -*- coding: utf-8 -*-

"""Tests for the LetterCount Statistics Generator module"""

from typing import List
import unittest

from text_statistics import LetterCount
from .base_stats_generator_test import BaseStatsGeneratorTest
from .unit_test_data import UnitTestData


class TestLetterCount(BaseStatsGeneratorTest, unittest.TestCase):
    """Test the LetterCount plugin using the python unittest framework."""

    @property
    def stats_generator_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects for BaseStatsGeneratorTest to test.
        """
        return [
            UnitTestData('No Letters', [''], expected_result=0),
            UnitTestData('One Letter', ['A'], expected_result=1),
            UnitTestData(
                'Multiple Letters',
                ['Hello, World!'],
                expected_result=10
            ),
            UnitTestData(
                'Numbers',
                ['There were 101 tests'],
                expected_result=17
            ),
            UnitTestData(
                'Multiple Lines',
                [
                    'This is the first line\n',
                    'And this is the second line',
                ],
                expected_result=40
            ),
            UnitTestData(
                'UTF-8 String',
                ['È in italiano'],
                expected_result=11
            ),
            UnitTestData(
                'Non-Latin Charset',
                ['它是中文的'],
                expected_result=5
            ),
        ]

    @staticmethod
    def get_stats_generator() -> LetterCount:
        """Return a new LetterCount object."""
        return LetterCount()
