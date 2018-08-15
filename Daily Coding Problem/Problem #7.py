# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


import random

def pick(big_stream):
    random_element = None

    for index, elem in enumerate(big_stream):
        if index == 0:
            random_element = elem
        elif random.randint(1, index + 1) == 1:
            random_element = elem
        # print(index, elem)
    print(random_element)


big_stream = [1,2,3,4,5,6]

pick(big_stream)