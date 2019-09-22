# -*- coding: utf-8 -*-

from typing import Dict

from .statistics_generator import StatisticsGenerator

# Create a type alias to reduce the length a bit
StatsGenerators = Dict[str, StatisticsGenerator]


class TextStatistics:
    def __init__(self, file_name: str,
                 stats_generators: StatsGenerators) -> None:

        self.file_name: str = file_name
        self.stats_generators: StatsGenerators = stats_generators

    def process_file(self) -> None:
        with open(self.file_name, 'r') as file_handle:
            for line in file_handle:
                for stats_generator in self.stats_generators.values():
                    stats_generator.parse_line(line)
