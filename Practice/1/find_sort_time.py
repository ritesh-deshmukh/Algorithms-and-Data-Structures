import time
import random

arr1 = [x for x in range(0, 10000)]
random.shuffle(arr1)
epoch_time1 = int(time.time())
arr1.sort()
epoch_time2 = int(time.time())

# print(int((int(time2) - int(time1))))


print(epoch_time2-epoch_time1)