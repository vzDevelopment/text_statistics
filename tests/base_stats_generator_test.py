# -*- coding: utf-8 -*-

"""Provides an abstract class to help with testing plugins."""

from abc import ABC, abstractmethod
from typing import Any, List

from text_statistics import StatisticsGenerator
from .unit_test_data import UnitTestData


class BaseStatsGeneratorTest(ABC):
    """A base class than can be inherited to help test plugin classes.

    The class is designed to be used with Python's unittest framework.

    This abstract class provides a ``test_stats_generator`` method which tests
    the plugin with the tests defined in the ``stats_generator_tests``
    property. You need to override the ``stats_generator_tests`` property to
    return the tests you want to run and you will also need to override the
    ``get_stats_gernerator`` method so it returns the correct plugin object.
    """

    @property
    @abstractmethod
    def stats_generator_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects to test.

        Override this so it returns a list of tests we want to run.

        Example:
            return [
                UnitTestData('Test Name', ['example input'], 'expected_result')
            ]
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_stats_generator() -> StatisticsGenerator:
        """Returns an instance of the StatsGenerator Plugin we want to test.

        Override this so it returns the correct object that is being tested

        Example:
            return WordCount()
        """
        raise NotImplementedError()

    def test_stats_generator(self) -> None:
        """Test all the entries in the ``stats_generator_tests`` property."""
        for test in self.stats_generator_tests:
            # subTest will be implemented when this class is mixed into
            # unittest.TestCase
            with self.subTest(lines=test.lines):  # type: ignore[attr-defined] # pylint: disable=no-member
                stats_generator = self.get_stats_generator()

                for line in test.lines:
                    stats_generator.parse_line(line)

                actual_result: Any = stats_generator.result()
                # assertEqual will be implemented when this class is mixed into
                # unittest.TestCase
                self.assertEqual(  # type: ignore[attr-defined] # pylint: disable=no-member
                    actual_result,
                    test.expected_result,
                    "'{}' test failed. Got: '{}' but expected: '{}'".format(
                        test.name, actual_result, test.expected_result
                    )
                )
