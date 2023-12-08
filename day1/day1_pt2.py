calibration_input_file = "test_input1.txt"

calibration_values = 0

calibration_value_list = []

letter_num_dict = {"one":1, "two":2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight":8, "nine":9}

with open(calibration_input_file, mode="r") as file:
    for line in file.readlines():
        #print(line)
        line_nums = []
        for i,char in enumerate(line):
            if char.isdigit():
                line_nums.append(str(char))
            else:
                for key in letter_num_dict:
                    try:
                        new_string = line[i:i+len(key)]
                        #print(new_string)
                        if new_string == key:
                            line_nums.append(str(letter_num_dict[key]))
                    except IndexError:
                        pass
        if len(line_nums)<2:
            line_nums.append(line_nums[0])
        #print(line_nums)
        calibration_value = int(line_nums[0] + line_nums[-1])
        calibration_value_list.append(calibration_value)

#print(calibration_value_list)
for value in calibration_value_list:
    calibration_values += value

print(calibration_values)