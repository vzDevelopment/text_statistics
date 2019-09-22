# -*- coding: utf-8 -*-

"""Tests for the MostCommonLetter Statistics Generator module"""

from typing import List
import unittest

from text_statistics import MostCommonLetter
from .base_stats_generator_test import BaseStatsGeneratorTest
from .unit_test_data import UnitTestData


class TestMostCommonLetter(BaseStatsGeneratorTest, unittest.TestCase):
    """Test the MostCommonLetter plugin using the python unittest framework."""

    @property
    def stats_generator_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects for BaseStatsGeneratorTest to test.
        """
        return [
            UnitTestData('No Letters', [''], expected_result=set()),
            UnitTestData(
                'Multiple Letters',
                ['Hello, World!'],
                expected_result={'l'}
            ),
            UnitTestData(
                'Multiple Common Letters',
                ['abc'],
                expected_result={'a', 'b', 'c'}
            ),
            UnitTestData('Ignores Case', ['aa bBb CC'], expected_result={'b'}),
            UnitTestData(
                'Ignores Symbols',
                ['Symbols!!!!'],
                expected_result={'s'}
            ),
            UnitTestData(
                'Ignores Numbers',
                ["1000000000000000000 is a big number"],
                expected_result={'b', 'i'}
            ),
            UnitTestData(
                'Diacritical Marks',
                ["èe"],
                expected_result={'è', 'e'}
            ),
            UnitTestData(
                'Multiple Lines',
                [
                    'This is the first line\n',
                    'And this is the second line',
                ],
                expected_result={'i'}
            ),
            UnitTestData(
                'UTF-8 String',
                ['È in italiano'],
                expected_result={'i'}
            ),
            UnitTestData(
                'Non-Latin Charset',
                ['你好'],
                expected_result={'你', '好'}
            ),
        ]

    @staticmethod
    def get_stats_generator() -> MostCommonLetter:
        """Return a new MostCommonLetter object."""
        return MostCommonLetter()
