# -*- coding: utf-8 -*-

"""Provides an abstract class to help with testing plugins."""

from abc import ABC, abstractmethod
from typing import Any, List

from text_statistics import StatisticsGenerator
from .unit_test_data import UnitTestData


class BasePluginTest(ABC):
    """A base class than can be inherited to help test plugin classes.

    The class is designed to be used with Python's unittest framework.

    This abstract class provides a ``test_plugin`` method which tests the
    plugin with the tests defined in the ``plugin_tests`` property. You need to
    override the ``plugin_tests`` property to return the tests you want to run
    and you will also need to override the ``initialise_plugin`` method so it
    knows how to reset/create a new plugin object.
    """

    @property
    @abstractmethod
    def plugin_tests(self) -> List[UnitTestData]:
        """A list of UnitTestData objects to test.

        The UnitTestData objects contain the name of the test, data to be
        parsed, and the expected output.

        Example:
            return [
                UnitTestData('Test Name', ['example input'], 'expected_result')
            ]
        """
        return []

    @abstractmethod
    def initialise_plugin(self) -> None:
        """Creates the ``plugin`` property.

        Running this should also clear the previous plugin object's state.

        Example:
            self.plugin = Plugin()
        """
        # This is an abc.abstractmethod and cannot run so ignore the
        # type error given by mypy
        self.plugin: StatisticsGenerator = None    # type: ignore[arg-type]

    def test_plugin(self) -> None:
        """Test all the entries in the ``plugin_tests`` property."""
        for test in self.plugin_tests:
            # subTest will be implemented when this class is mixed into
            # unittest.TestCase
            with self.subTest(lines=test.lines):  # type: ignore[attr-defined] # pylint: disable=no-member
                # Erase the state from the previous tests
                self.initialise_plugin()

                for line in test.lines:
                    self.plugin.parse_line(line)

                actual_result: Any = self.plugin.result()
                # assertEqual will be implemented when this class is mixed into
                # unittest.TestCase
                self.assertEqual(  # type: ignore[attr-defined] # pylint: disable=no-member
                    actual_result,
                    test.expected_result,
                    "'{}' test failed. Got: '{}' but expected: '{}'".format(
                        test.name, actual_result, test.expected_result
                    )
                )
