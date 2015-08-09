__author__ = 'minh'
'''
weighted_random module makes it easier to do weighted random
'''
import random


#weighted choices takes in a dictionary of choices to weight
#and returns randomly a choice given by weights
def weighted_choice(weights):
    #stupid way to doing this,