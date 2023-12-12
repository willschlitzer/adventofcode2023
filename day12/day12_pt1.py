from example_input1 import example_string

data_list = example_string.split()

data_breakdown = [x.split(" ") for x in data_list]

print(data_breakdown)
