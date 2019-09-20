# -*- coding: utf-8 -*-

"""Tests for the LineCount Statistics Generator module"""

import unittest

from text_statistics import LineCount
from .base_plugin_test import BasePluginTest
from .unit_test_data import UnitTestData


class TestLineCount(BasePluginTest, unittest.TestCase):
    """Test the LineCount plugin using the python unittest framework."""

    @property
    def plugin_tests(self):
        """A list of UnitTestData objects for BasePluginTest to test."""
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
        ]

    def initialise_plugin(self):
        """Create a new LineCount object."""
        self.plugin = LineCount()
