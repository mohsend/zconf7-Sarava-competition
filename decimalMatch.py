#!/bin/en python3

# Author(s): Mohsen Dastjerdi Zade (me@mehsen.com)
# License: MIT
# Initial writing: 2016-09-09
# Last Update: 2016-09-09

class decimalMatch:
    """A module to generate pairs of words and decimal coded version of the word
    and keep them in a dictionary (key-value pair) for later use."""

    def __init__(self):
        # Dictionary to keep the word-code pairs
        self._pairs = {}

    def __getattribute__(self,name):
        return object.__getattribute__(self, name)

    def allowedWord(this, word):
        """Check if the word is a valid english word"""
        word = word.upper().strip()
        for c in word:
            if c < 'A' or c > 'Z':
                raise ValueError("Input is not a valid english word.")
            else:
                return word

    def allowedDecimal(this, coded):
        """Check if the decimal string is a valid."""
        for c in coded:
            if c < '0' or c > '9':
                raise ValueError("Input is not a valid decimal string.")
            else:
                return coded

    def calculateDecimal(this, word):
        """Calculates (generates) the decimal coded string from word"""
        string = ""
        for c in word:
            # Convert each ascii character to integer
            # and the integer to string
            string += str(ord(c) - ord('A') + 1)
        return string

    def appendToList(this, word):
        """Gets a word, adds it and the decimal coded to the dictionary."""
        try:
            word = this.allowedWord(word)
            this._pairs[word] = this.calculateDecimal(word)
            return {word, this._pairs[word]}
        except ValueError as e:
            print(e)

    def findInList(this, coded):
        """Gets a decimal string, returns the possible words in the dictionary."""
        try:
            coded = this.allowedDecimal(coded)
            temp = []
            for t in this._pairs:
                if this._pairs[t] == coded:
                    temp.append(t)
            return temp
        except ValueError as e:
            print(e)

def printHelp():
    print ("This is a module to generate pairs of words and decimal coded version of the word and keep them in a dictionary (key-value pair).")
    print ("Commands:")
    print ("\033[1madd   \"word\"\033[0m        Add word to set")
    print ("\033[1mfind  \"decimal\"\033[0m     Find word based on decimal code")
    print ("\033[1mset\033[0m                 Print the whole set")
    print ("\033[1mhelp\033[0m                Show this help")
    print ("\033[1mexit\033[0m                Terminate program")

if __name__ == "__main__":
    printHelp()
    a = decimalMatch()
    while 1:
        userinput = input()
        inputlist = userinput.split()
        if inputlist[0] == "exit":
            break
        elif inputlist[0] == "set":
            print(a._pairs)
        elif inputlist[0] == "add":
            print(a.appendToList(inputlist[1]))
        elif inputlist[0] == "find":
            print(a.findInList(inputlist[1]))
        else:
            printHelp()
