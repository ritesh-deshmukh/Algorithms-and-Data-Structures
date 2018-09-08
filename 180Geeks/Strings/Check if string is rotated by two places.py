# Given two strings, the task is to find if a string ('a') can be obtained by rotating another string ('b') by two places.
# Input : a = "amazon"
#         b = "azonam"  // rotated anti-clockwise
# Output : 1
#
# Input : a = "amazon"
#         b = "onamaz"  // rotated clockwise
# Output : 1

a_str = "amazon"
b_str = "zonama"

a = list(a_str)
b = list(b_str)

count = 0

def check(a,b, count):
    len_a = len(a)
    len_b = len(b)

    for i in range(len_a):
        if a == b:
            if len_b-count == 2:
                print(f"Rotated by {len_b-count} places in clockwise pattern")
            else:
                print(f"Rotated by {len_b-count} places in clockwise pattern")
        else:
            b.insert(len_b+1, b.pop(i))
            count += 1
            check(a,b,count)
        return

check(a,b,count)
