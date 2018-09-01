# Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.
# The result is going to be very large, hence return the result in the form of a string.


arr = [3,30,34,5,9]
size = len(arr)

def large_num(arr,size):
    temp_arr = arr
    a = []

    for i in range(size):
        a.append(max(temp_arr))
        temp_arr.remove(max(temp_arr))

    my_lst_str = ''.join(map(str, a))
    print(my_lst_str)

large_num(arr,size)
