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


game_id_count = 0

with open(input_file, mode="r") as file:
    for line in file.readlines():
        game_id = int(re.findall("Game \d+", line)[0].replace("Game ", ""))
        green_count = max_color_count("green", line)
        blue_count = max_color_count("blue", line)
        red_count = max_color_count("red", line)
        if (
            (green_count <= max_green)
            and (blue_count <= max_blue)
            and (red_count <= max_red)
        ):
            game_id_count += game_id

print(game_id_count)
