# -*- coding: utf-8 -*-

"""Calculates statistics for a given file."""

from typing import Dict

from .statistics_generator import StatisticsGenerator

# Create a type alias to reduce the length a bit
StatsGenerators = Dict[str, StatisticsGenerator]


class TextStatistics:
    """This class processes text files and generates statistics on the data.

    The statistics generated is plugable and you can control which statistics
    are provided by passing ``StatisticGenerator`` objects to the constructor.

    Attributes:
        stats_generators: A dictionary of id -> StatisticGenerator object
            mappings.
    """

    def __init__(self, stats_generators: StatsGenerators) -> None:
        """Initialise the class

        Arguments:
            stats_generators: This is a dictionary containing an id to
            StatisticsGenerator object mapping.
        """
        self.stats_generators: StatsGenerators = stats_generators

    def process_file(self, file_name: str) -> None:
        """Calculate statistics for the provided file name.

        This method will loop through each of the stats_generators and
        calculate statistics for the provided file.

        Arguments:
            file_name: the location of the file to generate statistics for.
        """
        with open(file_name, 'r') as file_handle:
            for line in file_handle:
                for stats_generator in self.stats_generators.values():
                    stats_generator.parse_line(line)
