#!/usr/bin/python
"""
random sentence generator using first order markov chain + a file
"""

import string

class sentenceGenerator:
    def __init__(self, file_name):
        #opening file
        file = open(file_name)
        #raw text
        raw = file.read()
        self.words = sentenceGenerator.process_raw_string(self,raw)
        

    def process_raw_string(self, raw):
        #make to lowercase and removes punctuation
        #and splits it into list of words
        return raw.lower().translate(str.maketrans("","",
                string.punctuation)).split()
    def generateMarkov(self):
        print (self.words)
