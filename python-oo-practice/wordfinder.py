"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary
    >>> wf = WordFinder("simple.txt")
    3 words read
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

import random

class WordFinder:
    """Machine for finding random words from a dictionary."""
    
    def __init__(self, path):
        """Read dictionary and report number of items read."""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print("{} words read".format(len(self.words)))

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""
        return random.choice(self.words)

# Create an instance of WordFinder with the path to words.txt
wf = WordFinder("words.txt")

# Test the random() method
print(wf.random())
print(wf.random())
print(wf.random())


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments."""
    
    def parse(self, dict_file):
        """Parse dict_file -> list of wrods,skipping blanks/comments."""

        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
    

swf = SpecialWordFinder("complex.txt")

print(swf.random())
print(swf.random())
print(swf.random())

