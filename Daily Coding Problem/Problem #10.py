# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time
import sched

all_time = sched.scheduler(time.time, time.sleep)

def return_function(name, start):
    curr = time.time()
    new_curr = int(curr-start)
    print(f"\nJob Scheduled on: {time.ctime(curr)}, Time Elasped: {new_curr}, Job Name: {name}")


curr_time = time.time()
if all_time.empty():
    print("No events scheduled currently")

print("")
print(f"Loading scheduled events starting at time: {time.ctime(curr_time)}")
all_time.enter(2,1,return_function, ("Do something(1)", curr_time))
display_text = "Job Schedule Details below"
if not all_time.empty():
    print(display_text)
    for _ in range(len(display_text)+1):
        print("-", end="")
    # print("\n")
# print(all_time.queue)
all_time.enter(3,1,return_function, ("Do something(2)", curr_time))
all_time.enter(4,1,return_function, ("Do something(3)", curr_time))
all_time.run()