# -*- coding: utf-8 -*-

"""Tests for the AverageWordSize Statistics Generator module"""

from typing import List
import unittest

from text_statistics import AverageWordSize
from .base_stats_generator_test import BaseStatsGeneratorTest
from .unit_test_data import UnitTestData


class TestAverageWordSize(BaseStatsGeneratorTest, unittest.TestCase):
    """Test the AverageWordSize plugin using the python unittest framework."""

    @property
    def stats_generator_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects for BaseStatsGeneratorTest to test.
        """
        return [
            UnitTestData('No Words', [''], expected_result=0.0),
            UnitTestData('One Word', ['Hello'], expected_result=5.0),
            UnitTestData(
                'Multiple Words',
                ['Lorem ipsum dolor sit amet'],
                expected_result=4.4
            ),
            UnitTestData(
                'Multiple Lines',
                [
                    'This is the first line\n',
                    'And this is the second line',
                ],
                expected_result=3.6
            ),
            UnitTestData(
                'UTF-8 String',
                ['È in italiano'],
                expected_result=3.7
            ),
            UnitTestData(
                'Non-Latin Charset',
                ['它是中文的'],
                expected_result=5
            ),
        ]

    @staticmethod
    def get_stats_generator() -> AverageWordSize:
        """Return a new AverageWordSize object."""
        return AverageWordSize()

    def test_decimal_places(self) -> None:
        """Test the decimal_place constructor parameter."""
        stats_generator: AverageWordSize = AverageWordSize(decimal_places=3)
        stats_generator.parse_line('Test Decimal Places')
        expected_result: float = 5.667

        self.assertEqual(
            stats_generator.result(),
            expected_result
        )
