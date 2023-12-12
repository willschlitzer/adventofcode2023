import re

input_file = "test_input1.txt"

game_list = []

max_red = 12
max_green = 13
max_blue = 14


def max_color_count(color, line):
    color_count = 0
    x = re.findall(f"\d+ {color}", line)
    if len(x) == 0:
        return 0
    else:
        value_list = []
        for value in x:
            num_value = int(value.replace(color, ""))
            value_list.append(num_value)
    return max(value_list)


total_game_power = 0

with open(input_file, mode="r") as file:
    for line in file.readlines():
        game_id = int(re.findall("Game \d+", line)[0].replace("Game ", ""))
        green_count = max_color_count("green", line)
        blue_count = max_color_count("blue", line)
        red_count = max_color_count("red", line)
        game_power = green_count * red_count * blue_count
        total_game_power += game_power

print(total_game_power)
