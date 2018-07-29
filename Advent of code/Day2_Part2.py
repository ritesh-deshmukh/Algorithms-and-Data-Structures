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
        wrap_ribbon = (dimensions[0] + dimensions[0] + dimensions[1] + dimensions[1])
        bow_ribbon = (dimensions[0] * dimensions[1] * dimensions[2])
        total_ribbon = wrap_ribbon + bow_ribbon
        print(total_ribbon)
        # area = ((dimensions[0] + dimensions[0] + dimensions[1] + dimensions[1])
        #       + (dimensions[0] * dimensions[1] * dimensions[2]))
        total_area += total_ribbon
        # print(sorted)
    print(f"Ribbon total: {total_area}")