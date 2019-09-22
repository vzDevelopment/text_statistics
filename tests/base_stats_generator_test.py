# -*- coding: utf-8 -*-

"""Provides an abstract BaseStatsGeneratorTest Mixin to help test plugins.

This Mixin is used to reduce code duplication in the unit tests.
"""

from abc import ABC, abstractmethod
from typing import Any, List

from text_statistics import StatisticsGenerator
from .unit_test_data import UnitTestData


class BaseStatsGeneratorTest(ABC):
    """A base class than can be inherited to help test StatisiticsGenerators.

    Use this class as a Mixin with unittest.TestCase when testing
    StatisticGenerator subclasses to avoid code duplication.

    You will need to override the ``stats_generator_tests`` property so that it
    returns a list of UnitTestData objects you want to run the tests on. You
    will also need to override the ``get_stats_generator`` method so it returns
    an instance of the object you want to test.

    Example:
        class TestFoo(BaseStatsGeneratorTest, unittest.TestCase):
            def tests(self):
                ...

            @staticmethod
            def get_stats_generator():
                ...
    """
    @property
    @abstractmethod
    def stats_generator_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects to test.

        Override this so it returns a list of tests to run.

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
