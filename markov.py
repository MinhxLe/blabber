#!/usr/bin/python
"""
markovChain class attempts to produce a obj_list of resultects that
matches pattern of inputted obj_list of resultects
"""

import queue
import tools
import random

class markov_chain:
    def __init__(self, obj_list, level=1):
        self.level = level
        #no point in storing obj_list variable
        self.pair_tb = {}
        self.__fill_pair_tb(obj_list)
        #need a random obj to start off
        self.start = random.choice(obj_list)

    def __fill_pair_tb(self, obj_list):
        #cache stores words read until full and then
        #stores in m_raw_count_tb
        temp_caches = []
        #generate caches
        for x in range(1,self.level + 1):
            temp_caches.append(queue.Queue(x))
        for result in obj_list:
            for c in temp_caches:
                if c.full():
                    pattern = tuple(c.queue)
                    if pattern in self.pair_tb:
                        if result in self.pair_tb[pattern]:
                            self.pair_tb[pattern][result] += 1
                        else:
                            self.pair_tb[pattern][result] = 1
                    else:
                        self.pair_tb[pattern] = {}
                        self.pair_tb[pattern][result] = 1
                    #removes first item and put result at the end
                    c.get()
                    c.put(result)
                else:
                    c.put(result)

    def __debug_pair_tb(self):

        for i in self.pair_tb:
            for o in i:
                print(i)
                print(o)
                print (self.pair_tb[i][o])

    def generate_obj_list(self, count = 10):
        cache = queue.Queue(self.level)
        cache.put(self.start)
        print(self.start)
        for x in range(1, count):
            pattern = [obj for obj in cache.queue]
            #returns longest pattern from history
            while not tuple(pattern) in self.pair_tb:
                pattern.pop()
            new_obj = tools.weighted_choice(self.pair_tb[tuple(pattern)])
            print (new_obj)
            #updates cache
            if cache.full():
                cache.get()
            cache.put(new_obj)






