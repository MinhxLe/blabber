__author__ = 'minh'
'''
weighted_random module makes it easier to do weighted random
'''
import random


#weighted choices takes in a dictionary of choices to weight
#and returns randomly a choice given by weights(ints)
def weighted_choice(weights):
    #stupid way to doing this, I know
    m_list = []
    for obj in weights:
        for times in range(0, weights[obj]):
            m_list.append(obj)
    return random.choice(m_list)