# -*- coding: utf-8 -*-

"""Tests for the LetterCount Statistics Generator module"""

from typing import List
import unittest

from text_statistics import LetterCount
from .base_plugin_test import BasePluginTest
from .unit_test_data import UnitTestData


class TestLetterCount(BasePluginTest, unittest.TestCase):
    """Test the LetterCount plugin using the python unittest framework."""

    @property
    def plugin_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects for BasePluginTest to test."""
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

    def initialise_plugin(self) -> None:
        """Create a new LetterCount object."""
        self.plugin: LetterCount = LetterCount()
