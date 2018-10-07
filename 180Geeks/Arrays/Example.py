# Example: Input: "[1,2,3]" Output: "6   3   2"

arr = [1,2,3]
arr1 = arr[:]
ans = []

# for i in range(len(arr)+1):
#     if i+1 == len(arr):
#         ans.append(arr[-1]*arr[0])
#     else:
#         ans.append(arr[i]*arr[i+1])
# print(ans)

def mult(arr1, ans, arr):
    if len(arr1) == 1:
        ans.append(arr1[0]*arr[0])
    else:
        ans.append(arr1[0]*arr1[1])
        arr1.remove(arr1[0])
        mult(arr1,ans,arr)

mult(arr1,ans,arr)
print(ans)
temp = ans[0]
ans.remove(ans[0])
print(ans)
ans.append(temp)
print(ans)
new_temp =  " ".join(map(str, ans))
print(new_temp)
