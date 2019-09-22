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

# List of stats we want to obtain
stats_generators = [
    text_statistics.AverageWordSize(),
    text_statistics.LetterCount(),
    text_statistics.LineCount(),
    text_statistics.MostCommonLetter(),
    text_statistics.WordCount(),
]
stats = text_statistics.TextStatistics(args.file, stats_generators)

stats.process_file()

for stats_generator in stats.stats_generators:
    print(f"{stats_generator}")
