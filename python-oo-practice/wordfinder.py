"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''Module for finding random words from a dictionary'''


    def __init__(self, path):
        '''Read provided dictionary and tell how many words were found'''
        dictFile = open(path)

        self.words = self.parse(dictFile)

        print(f'{len(self.words)} words were read')

    def parse(self,dictFile):
        '''Parse the words from the provided file into a list'''
        return [words.strip() for words in dictFile]
    
    def random(self):
        '''Pick a random word from the file'''
        return random.choice(self.words)
    
class SpecialWordFinder:
    '''Same wordfinder functionality while not including blank lines or comments'''
    def parse(self,dictFile):
        '''Parse the words from the provided file into a list skipping blank lines and comments'''
        return [words.strip() for words in dictFile if words.strip() and not words.startswith('#')]