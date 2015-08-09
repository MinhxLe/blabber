#!/usr/bin/python
import markov



def main():
    a = [1,3,45,5,121,2,1,2,2,4,1,1,1,23,4,1,1,1,1,1,1,1,1]
    m = markov.markov_chain(a,3)


if __name__ == "__main__":
    main()
