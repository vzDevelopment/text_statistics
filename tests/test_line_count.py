# -*- coding: utf-8 -*-

"""Tests for the LineCount Statistics Generator module"""

from typing import List
import unittest

from text_statistics import LineCount
from .base_stats_generator_test import BaseStatsGeneratorTest
from .unit_test_data import UnitTestData


class TestLineCount(BaseStatsGeneratorTest, unittest.TestCase):
    """Test the LineCount plugin using the python unittest framework."""

    @property
    def stats_generator_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects for BaseStatsGeneratorTest to test.
        """
        return [
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
            UnitTestData(
                'Windows line endings',
                [
                    'Line1\r\n',
                    'Line2\r\n',
                ],
                expected_result=2
            ),
        ]

    @staticmethod
    def get_stats_generator() -> LineCount:
        """Return a new LineCount object."""
        return LineCount()
