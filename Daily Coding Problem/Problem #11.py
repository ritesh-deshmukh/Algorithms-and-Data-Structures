# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

times = [(30, 75), (0, 50), (60, 150)]

def min_rooms(times):
    count = 0
    time_dict = {}
    start_times = [] * len(times)
    end_times = [] * len(times)
    for time in times:
        time_dict[time[1]] = time[0]
        start_times.append(time[0])
        end_times.append(time[1])
    # for key in sorted(time_dict):
        # print("%s: %s" % (key, time_dict[key]))
    # print(start_times)
    # print(end_times)
    # print(time_dict)
    new_endtimes = sorted(end_times)
    print(new_endtimes)
    for i in range(len(end_times)):
        if time_dict[new_endtimes[i]] < new_endtimes[i+1]:
            count += 1
            print("Room")
        else:
            print("No room")
        print(count)

min_rooms(times)


