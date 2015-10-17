#!/usr/bin/python
import sentence_generator



def main():
    test = sentence_generator.sentence_generator("harrypotter.txt",2)
    test.generate_sentence(100)

if __name__ == "__main__":
    main()
