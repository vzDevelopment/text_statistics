#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
A simple script demonstrating how to use the text_statistics module.

Usage: ./example $text_file
"""

import argparse

import text_statistics

arg_parser = argparse.ArgumentParser('Produce statistics on a text file.')
arg_parser.add_argument(
    'file', type=str,
    help='Text file to obtain stats for.'
)
args = arg_parser.parse_args()

# Dictionary of stats we want to obtain
stats_generators = {
    'Average Word Size': text_statistics.AverageWordSize(),
    'Letter Count': text_statistics.LetterCount(),
    'Line Count': text_statistics.LineCount(),
    'Most Common Letter': text_statistics.MostCommonLetter(),
    'Word Count': text_statistics.WordCount(),
}
stats = text_statistics.TextStatistics(args.file, stats_generators)

stats.process_file()

# Print all stats
for identifier, stats_generator in stats.stats_generators.items():
    print(f"{identifier}: {stats_generator}")

# Create your own stats
words = stats.stats_generators.get('Word Count').result()
lines = stats.stats_generators.get('Line Count').result()
words_per_line = words / lines

print(f"Words per line: {words_per_line}")
