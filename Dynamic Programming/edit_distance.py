# Given two strings str1 and str2 and below operations that can performed on str1.
# Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
# Insert
# Remove
# Replace


def edDist(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edDist(str1, str2, m-1, n-1)

    return 1 + min(edDist(str1, str2, m, n-1),      # Insert
                   edDist(str1, str2, m-1, n),      # Remove
                   edDist(str1, str2, m-1, n - 1)   # Replace
                   )


str1 = "sunday"
str2 = "saturday"
print(edDist(str1, str2, len(str1), len(str2)))

