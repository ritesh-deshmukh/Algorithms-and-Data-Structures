# count the number of vowels present in a list

lst = ['a', 'e', 'i', 'o', 'u']
ex = "text"
text = list(ex)
count = 0

for i in range(len(text)):
    if text[i] in lst:
        print(f"Found, {text[i]}")
        count += 1
    else:
        print("not found")

print(count)