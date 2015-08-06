#!/usr/bin/python
from markov import sentenceGenerator
def main():
    
    m_generator = sentenceGenerator("words.txt")
    m_generator.generateMarkov()

if __name__ == "__main__":
    main()
