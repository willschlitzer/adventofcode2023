calibration_input_file = "test_input1.txt"

calibration_values = 0

calibration_value_list = []

with open(calibration_input_file, mode="r") as file:
    for line in file.readlines():
        line_nums = []
        for char in line:
            if char.isdigit():
                line_nums.append(str(char))
        if len(line_nums) < 2:
            line_nums.append(line_nums[0])
        calibration_value = int(line_nums[0] + line_nums[-1])
        calibration_value_list.append(calibration_value)

# print(calibration_value_list)
for value in calibration_value_list:
    calibration_values += value

print(calibration_values)
