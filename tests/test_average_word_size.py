# -*- coding: utf-8 -*-

"""Tests for the AverageWordSize Statistics Generator module"""

import unittest

from text_statistics import AverageWordSize
from .base_plugin_test import BasePluginTest
from .unit_test_data import UnitTestData


class TestAverageWordSize(BasePluginTest, unittest.TestCase):
    """Test the AverageWordSize plugin using the python unittest framework."""

    @property
    def plugin_tests(self):
        """A list of UnitTestData objects for BasePluginTest to test."""
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

    def initialise_plugin(self):
        """Create a new AverageWordSize object."""
        self.plugin = AverageWordSize()

    def test_decimal_places(self):
        """Test the decimal_place constructor parameter."""
        plugin = AverageWordSize(decimal_places=3)
        plugin.parse_line('Test Decimal Places')
        expected_result = 5.667

        self.assertEqual(
            plugin.result(),
            expected_result
        )
