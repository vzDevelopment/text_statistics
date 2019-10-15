# Text Statistics

## About
This library allows the user to compute various statistics about a text file. For example, it can calculate:

* The whitespace delimited word count
* The line count
* The average number of lines per word
* The most common letters

The library can easily be extended to provide additional statistics.

### Background
This was a coding exercise which I have used for practise. The original specification was to write a library to compute some statistics about a local text file with the aim of it being easy to extend to compute additional statistics in the future.

## Requirements

* Python 3.7 or later

## How to use

### Quick Start

If you just want to see the library in action, then just run `example.py` as explained in the [example.py section](#examplepy) below.

### Installing the package
If you don't have a source archive file you can build one by following the `Building the package` section. You can then install this with pip e.g.

```
pip3 install ./dist/text_statistics-0.1.0.tar.gz
```

Alternatively, you can just ensure the package is in your path (`sys.path`). For example, running `./example.py` with the currently directory layout will work fine because Python will look for the module in directory containing the script.

### Running the code

First create an instance of the `TextStatistics` class, passing in a dictionary with the Statistics Generator objects you want to run. For example, if you want to get the word and line counts use:

```
stats = text_statistics.TextStatistics({
	'Word Count': text_statistics.WordCount(),
	'Line Count': text_statistics.LineCount(),
})
```

The key for the dictionary is an identifier which you can use to obtain the individual statistic at a later date if you wish.

Once you have done this, parse the text file you want to obtain statistics about:

```
stats.process_file('/path/to/your/file.txt')
```

_if you want to combine the statistics for multiple files, run the `process_file` method for each file._

You can then print out all the statistics:

```
for identifier, stats_generator in stats.stats_generators.items():
    print(f"{identifier}: {stats_generator}")
```

You could also get individual statistics:

```
words = stats.get('Word Count').result()
lines = stats.get('Line Count').result()

words_per_line = words / lines
```

### example.py
I've included a very basic example.py script demonstrating the use explained above. To run it use:

```
./example.py example_file.txt
```

## Plugins/Statistics Generators

The currently available Statistic Generators are:

### AverageWordSize
Provides the average number of letters per word.

This plugin considers a letter to be an alphabetical or numerical character (i.e. [str.isalnum()](https://docs.python.org/3/library/stdtypes.html#str.isalnum)). Numerical characters are included becase numbers are included in the word count. This means the end stat will make more sense in sentences such as _"she saw 6 monkeys, 10 lions, and 4 rhinos at the safari park."_

### LineCount
Provides the number of lines in a file.

### LetterCount
Calculates the number of alphabetical and numerical characters (i.e. [str.isalnum()](https://docs.python.org/3/library/stdtypes.html#str.isalnum)) in the file.

### LetterOccurances
Counts the number of alphabetical characters (as per [str.isalpha()](https://docs.python.org/3/library/stdtypes.html#str.isalpha)) in a file and returns the counts in a dictionary.

### MostCommonLetter
Returns a set of the most common alphabetical characters (as defined in LetterOccurances) in a file.

### WordCount
Returns the number of whitespace delimited words in a file.

## Developers Guide

### Testing
The library uses the standard [unittest](https://docs.python.org/3/library/unittest.html) module provided by Python. To run the unit tests, run the following command:

```
python3 -m unittest discover
```

_n.b. replace `python3` with the correct command for python version 3 on your operating system._

### Creating a new statistics generator plugin

To create a new plugin, all you need to do is inherit from the `StatisticsGenerator` class and implement the `parse_line` and `result` methods.

### Static type analysis
The code uses Python's type hints and can be analysed with static type checkers such as [mypy](http://mypy-lang.org/).

### Dev Reports

The following commands will install and run the dev report tools:

```
pip3 install -r requirements/dev.txt
make dev-report
```

This will run type checking, normal linting, security linting, the unit tests, perform mutation testing, and produce a unit test coverage report in `htmlcov/`.

### Building the package

You can either install the dev dependencies and run the entire build pipeline:

```
pip3 install -r requirements/dev.txt
make build
```

or build the package yourself using Python's [setuptools](https://packaging.python.org/key_projects/#setuptools) e.g.

```
python3 setup.py sdist bdist_wheel
```

Both methods will put the built files in the `dist/` directory.

## Caveats

As the library is designed for producing text statistics for a human readable text file, it reads a file in line-by-line. Therefore, if you provide it with a file with a very large line e.g. a binary file with just the one line, then it will read this all into memory. I considered reading in a configurable amount of bytes instead, but this over-complicates the plugins e.g. trying to find the word count but the read operation has only read half the word.

I'm enforcing a standard interface for the plugins e.g. they must provide a `parse_line` method. However, this means if you want to add a method to this interface, you will need to add it to all the plugins - otherwise they will break.
