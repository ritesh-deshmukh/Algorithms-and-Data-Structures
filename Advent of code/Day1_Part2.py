# input_task = input("Enter Directions String: ")

f = open("santa_input", "r")

if f.mode == "r":
    input_task = f.read()

print(f"Input is: {input_task}")

rules = ["(", ")"]

final_floor = 0

for i in range(len(input_task)):
    if final_floor == -1:
        print(f"Santa reached the basement at: {i}")
        break
    if input_task[i] is rules[0]:
        final_floor += 1
    else:
        final_floor -= 1

print(f"The destination floor for santa is: {final_floor}")


