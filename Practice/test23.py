import operator

class Rare:

    @staticmethod
    def nth_most_rare(elements, n):
        dict1 = {}
        for each in elements:
            if each in dict1:
                dict1[each] += 1
            else:
                dict1[each] = 1

        sorted_dict = sorted(dict1.items(), key=operator.itemgetter(1))

        if n < len(dict1):
            return_arr = []
            for item in sorted_dict:
                if item[1] == n:
                    return_arr.append(str(item[0]))
            return ", ".join(return_arr)
        else:
            return " "


print(Rare.nth_most_rare([1,1,1,2,2,3,3], 2))

# import operator
#
# class Rare:
#
#     @staticmethod
#     def nth_most_rare(elements, n):
#         dict1 = {}
#         for each in elements:
#             if each in dict1:
#                 dict1[each] += 1
#             else:
#                 dict1[each] = 1
#
#         sorted_dict = sorted(dict1.items(), key=operator.itemgetter(1))
#         if n < len(dict1):
#             return sorted_dict[n-1][1]
#         else:
#             return None
#
#
# print(Rare.nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))