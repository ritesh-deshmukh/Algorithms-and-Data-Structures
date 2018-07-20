# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?


given_array = [3, 2, 0, 1]
n = len(given_array)

def prodArray(given_array):
    product = 1
    for x in range(len(given_array)):
        if given_array[x] == 0:
            pos_zero = x
            given_array[x] = 1
        product *= given_array[x]

    given_array[pos_zero] = product


    # for y in range(len(given_array[:pos_zero])):
    #     given_array[y] = 0

    # for z in range(len(given_array[pos_zero:])):
    #     given_array[z] = 0
        # if given_array[y] == 0:
        #     given_array[y] = product
        #     break
        # else:
        #     pass
            # given_array[y] = product//given_array[y]

    print(given_array)

prodArray(given_array)


