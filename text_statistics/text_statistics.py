# -*- coding: utf-8 -*-


class TextStatistics:
    def __init__(self, file_name, stats_generators):
        self.file_name = file_name

        # TODO pass in multiple generators/list
        # TODO use a dictionary/its own class?
        self.stats_generators = stats_generators

    def process_file(self):
        with open(self.file_name, 'r') as file_handle:
            for line in file_handle:
                for stats_generator in self.stats_generators:
                    stats_generator.parse_line(line)
