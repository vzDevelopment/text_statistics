# -*- coding: utf-8 -*-

"""An interface for the Statistics Generator Plugins."""

from abc import ABC, abstractmethod
from typing import Any


class StatisticsGenerator(ABC):
    """This class provides an interface for Statistics Generator Plugins.

    Each class which calculates a statistic for the TextStatistics module
    should inherit the interface from this class so that it's enforced.

    The caller will call the ``parse_line`` method for every line seen in the
    text file. Once the caller has finished parsing lines, it will call the
    ``result`` method to obtain the statistics that the plugin is calculating.
    """

    @abstractmethod
    def parse_line(self, line: str) -> None:
        """Parse a line from a text file.

        This method is called for every line in a text file. The subclass
        should override this class and generate statistics from the data.
        """
        raise NotImplementedError()

    @abstractmethod
    def result(self) -> Any:
        """Return the result from the parsed data."""
        raise NotImplementedError()

    def __str__(self) -> str:
        """Return the result as a string."""
        return f"{self.result()}"
