from example_input1 import example_string
import re

data = example_string.split()

empty_line_index_list = []

for i, line in enumerate(data):
    if "#" not in line:
        empty_line = line
        empty_line_index_list.append(i)

# print(empty_line_index_list)
# print(empty_line_index_list[-1::-1])
for i in empty_line_index_list[-1::-1]:
    data.insert(i, empty_line)

# print(data)

distance_lists = []

galaxy_list = []

for iy, line in enumerate(data):
    for ix, char in enumerate(line):
        if char == "#":
            galaxy_list.append([ix, iy])

print(galaxy_list)

total_distance = 0

for _ in range(9):
    galaxy_distance_list = []
    galaxy = galaxy_list.pop(0)
    for galaxy_2 in galaxy_list:
        dx = abs(galaxy_2[0] - galaxy[0] + 1)
        dy = abs(galaxy_2[1] - galaxy[1] + 1)
        galaxy_distance_list.append(dx + dy)
    print(galaxy_distance_list)

    total_distance += sum(galaxy_distance_list)

print(total_distance)
