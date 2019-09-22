# -*- coding: utf-8 -*-

"""Tests for the TextStatistics class."""

import unittest
from unittest.mock import Mock, mock_open, patch

from text_statistics import TextStatistics


class TestTextStatistics(unittest.TestCase):
    """Test the TextStatistics class."""

    def setUp(self) -> None:
        """Setup and create a TextStatistics object per test run."""
        self._stats = TextStatistics({
            'Mock Stats 1': Mock(),
            'Mock Stats 2': Mock(),
        })

    def test_process_file(self) -> None:
        """Test the process_file method works as expected."""

        mock_data: str = 'my_data'
        mock_file: str = 'my_file.txt'

        # Test file is opened once and read-only
        with patch('builtins.open', mock_open(read_data=mock_data)) \
                as mock_open_object:

            self._stats.process_file(mock_file)
            mock_open_object.assert_called_once_with(mock_file, 'r')

        # Test the stats generators' parse methods are called
        for stats_generator in self._stats.stats_generators.values():
            # The Mock confuses Mypy here so disable the type checking c.f.
            # https://github.com/python/mypy/issues/6713
            stats_generator.parse_line.assert_called_with(mock_data)  # type: ignore[attr-defined]
