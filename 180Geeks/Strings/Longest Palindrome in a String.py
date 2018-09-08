# Given a string S, find the longest palindromic substring in S.

str1 = "12wqabakl"
def long_pal(str1):
    maxLength = 1

    start = 0
    length = len(str1)

    low = 0
    high = 0

    # One by one consider every character as center point of
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and str1[low] == str1[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and str1[low] == str1[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    print("Longest palindrome substring is:",)

    print(str1[start:start + maxLength])

    return maxLength

print("Length is: " + str(long_pal(str1)))
