# -*- coding: utf-8 -*-

"""Provides a class to help with parameterized unit tests."""

from dataclasses import dataclass
from typing import Any, List


@dataclass(frozen=True)
class UnitTestData:
    """Stores data used in unit testing.

    Attributes:
        name: Human readable string describing the test.
        lines: Contains the data that should be tested. It should be
            represented as a list of strings where each entry in the list
            represents a line from the text being parsed.
        expected_result: The expected return value from the object.
    """
    name: str
    lines: List[str]
    expected_result: Any
