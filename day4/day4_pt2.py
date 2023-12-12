import re

input_file = "test_input1.txt"

card_score_list = []
card_count_list = []

with open(input_file, mode="r") as file:
    for line in file.readlines():
        #card_id = int(re.findall("Card \d+", line)[0].replace("Card ", ""))
        #print(card_id)
        card_split = line.split(":")
        game_split = card_split[1].split("|")
        winning_nums = [int(i) for i in game_split[0].strip().split()]
        card_nums = [int(i) for i in game_split[1].strip().split()]
        card_winning_count = 0
        card_score = 0
        for i in card_nums:
            if i in winning_nums:
                card_score += 1
        card_count_list.append(1)
        card_score_list.append(card_score)

print(card_count_list)

for i in range(len(card_count_list)):
    points = card_score_list[i]
    if points > 0:
        for _ in range(card_count_list[i]):
            for x in range(points):
                n = i + x + 1
                card_count_list[n] += 1
    #print(card_count_list)

#print("\n")
#print(card_count_list)
#print(card_score_list)
print(sum(card_count_list))
            
