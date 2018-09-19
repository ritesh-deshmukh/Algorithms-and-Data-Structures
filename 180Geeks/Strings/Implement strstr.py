# Your task  is to implement the function strstr.
# The function takes two strings as arguments(s,x) and  locates the occurrence of the string x in the string s.
# The function returns and integer denoting  the first occurrence of the string x .


str1 = "dtrfyguhjiokp"
str2 = "rfy"

def strstr(str1, str2):
    if str2 in str1:
        print(f"Found '{str2}' in '{str1}' at position: {str1.find(str2)+1}")
    else:
        print("Not found")

print(f"Find '{str2}' in '{str1}'")
strstr(str1,str2)