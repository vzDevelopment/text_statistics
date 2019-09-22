# -*- coding: utf-8 -*-

"""Tests for the WordCount Statistics Generator module"""

from typing import List
import unittest

from text_statistics import WordCount
from .base_plugin_test import BasePluginTest
from .unit_test_data import UnitTestData


class TestWordCount(BasePluginTest, unittest.TestCase):
    """Test the WordCount plugin using the python unittest framework."""

    @property
    def plugin_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects for BasePluginTest to test."""
        return [
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

    def initialise_plugin(self) -> None:
        """Create a new WordCount object."""
        self.plugin: WordCount = WordCount()
