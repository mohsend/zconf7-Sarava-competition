# decimalMatch

A Python 3 module to generate pairs of words and decimal coded version of the word
and keep them in a dictionary (key-value pair) for later use.

## Usage

Import this module to your python code after copying it in your python executable or project directory.

```python3
from decimalMatch import decimalMatch # Import

a = decimalMatch() # Create object

# API usage example:
a.appendToList("word") # Returns word-code pair
a.findInList("2315184") # Returns list of word-code pairs
a.pairs # dictionary of the word-code pairs
```

## CLI

There's a CommandLine Interface for this module. just Run `decimalMatch.py`

```
$ python3 decimalMatch.py
This is a module to generate pairs of words and decimal coded
version of the word and keep them in a dictionary (key-value pair).
Commands:
add   "word"        Add word to set
find  "decimal"     Find word based on decimal code
set                 Print the whole set
help                Show this help
exit                Terminate program
add word
{'WORD', '2315184'}
add another
{'ANOTHER', '11415208518'}
set
{'ANOTHER': '11415208518', 'WORD': '2315184'}
find 12
[]
find 2315184
['WORD']
exit
```

## Test

Just run `unitTest.py`.

```
$ python3 unitTest.py
.....
-------------------------------------------------
Ran 5 tests in 0.000s

OK
```

## Why?

This is my solution to [Sarava's coding competition at zconf7](competition.md).

## License

[decimalMatch](https://github.com/mohsend/zconf7-Sarava-competition) by [Mohsen Dastjerdi Zade](https://mehsen.com) is released under the terms of [MIT License](LICENSE).
