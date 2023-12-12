from example_input1 import example_string
import numpy as np
import math

# record_list = [[48, 98, 90, 83], [390, 1103, 1112, 1360]]
record_list = [[48989083], [390110311121360]]

winning_count_list = []

for i, time in enumerate(record_list[0]):
    winning_count = 0
    for charge_time in range(time):
        total_distance = charge_time * (time - charge_time)
        if total_distance > record_list[1][i]:
            winning_count += 1
    winning_count_list.append(winning_count)

print(winning_count_list)
# print(np.prod(winning_count_list))
