#!/usr/bin/python
"""
markovChain class attempts to produce a obj_list of resultects that
matches pattern of inputted obj_list of resultects
"""

import queue

class markov_chain:
    def __init__(self, obj_list, level=1):
        self.level = level
        #no point in storing obj_list variable
        self.pair_tb = {}
        self.fill_raw_tb(self, obj_list)
        #need a random obj to start off

    def fill_raw_tb(self, obj_list):
        #cache stores words read until full and then
        #stores in m_raw_count_tb
        temp_caches = []
        for x in range(1,self.level):
            temp_caches.append(queue.Queue(x))
        for result in obj_list:
            for c in temp_caches:
                if c.full():
                    pattern = [item for item in c.queue]
                    if pattern in self.pair_tb:
                        if result in self.pair_tb[pattern]:
                            self.pair_tb[pattern][result] += 1
                        else:
                            self.pair_tb[pattern][result] = 1
                    else:
                        self.pair_tb[pattern][result] = 1
                    #removes first item and put result at the end
                    c.get()
                    c.put(result)
                else:
                    c.put(result)


    def generate_obj_list(self, count):
        print("hi world")
        #generate seed


