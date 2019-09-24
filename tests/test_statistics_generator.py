# -*- coding: utf-8 -*-

"""Tests for the StatisticsGenerator class."""

import unittest

from text_statistics import StatisticsGenerator


class TestStatisticsGenerator(unittest.TestCase):
    """Test the StatisticsGenerator class."""

    def test_abstract_methods(self) -> None:
        """Test the class raises an exception when not subclassed.

        It should raise an exception if the parse_line and result methods
        haven't been implemented.
        """
        with self.assertRaises(TypeError) as error:
            StatisticsGenerator()  # type: ignore # pylint: disable=abstract-class-instantiated

        # Check the error matches what is expected e.g. this will help catch if
        # someone accidentally removed one of the @abstractmethod decorators
        expected_strings = [
            "Can't instantiate abstract class",
            "abstract methods parse_line, result",
        ]

        for expected_string in expected_strings:
            self.assertTrue(
                expected_string in str(error.exception),
                f"Did not find '{expected_string}' in exception error message"
            )

    def test_string_method(self) -> None:
        """Test the __str__ method."""

        # Use a number here so we can test it gets converted to a string
        example_result = 123

        # As StatisticsGenerator is an abstract class we need to create a
        # subclass to test the __str__ method - otherwise it'd throw an error
        # c.f. test_abstract_methods()
        class TestClass(StatisticsGenerator):
            """A class to test the instantiation of a StatisticsGenerator.

            This class is required as we can't instantiate an abstract class
            without implementing the abstract methods.
            """
            def parse_line(self, line) -> None:
                pass

            def result(self) -> int:
                return example_result

        test_class = TestClass()

        self.assertEqual(str(test_class), str(example_result))
