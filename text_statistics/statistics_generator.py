# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class StatisticsGenerator(ABC):
    def __init__(self, name):
        self._name = str(name)

    @property
    def name(self):
        return self._name

    @abstractmethod
    def parse_line(self, line):
        pass

    @abstractmethod
    def result(self):
        pass

    def __str__(self):
        return "{}: {}".format(self.name, self.result())
