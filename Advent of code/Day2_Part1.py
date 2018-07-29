# f = open("elves_input", "r")

# if f.mode == "r":
#     input_task = f.read()

# input_task = f.readlines()
# for symbol in input_task:
#     dimensions = symbol.split("x")
#     print(dimensions)

with open('elves_input') as f:
    dimensions_data = []
    for line in f:
        line = line.split('x') # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            dimensions_data.append(line)

    # product = dimensions_data[0][0]
    # print(dimensions_data[0])
    total_area = 0
    for dimensions in dimensions_data:
        # sorted = sorted(dimensions)
        # small_side_1 = sorted[0]
        # small_side_2 = sorted[1]
        area = ((2* dimensions[0] * dimensions[1])
              + (2* dimensions[1] * dimensions[2])
              + (2* dimensions[0] * dimensions[2]))
        total_area += area
        # print(sorted)
    print(f"Area total: {total_area}")

    total_small_side = 0
    for dimensions1 in dimensions_data:
        area1 = sorted(dimensions1)
        # print(area1[0] * area1[1])
        small_side = area1[0] * area1[1]
        total_small_side += small_side
    print(f"Small side total: {total_small_side}")

    answer = total_area + total_small_side
    print(f"Total Square feet: {answer}")