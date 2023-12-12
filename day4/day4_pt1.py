import re

input_file = "test_input1.txt"

total_card_score = 0

with open(input_file, mode="r") as file:
    for line in file.readlines():
        #card_id = int(re.findall("Card \d+", line)[0].replace("Card ", ""))
        #print(card_id)
        card_split = line.split(":")
        print(card_split)
        game_split = card_split[1].split("|")
        print(game_split)
        winning_nums = [int(i) for i in game_split[0].strip().split()]
        card_nums = [int(i) for i in game_split[1].strip().split()]
        card_winning_count = 0
        for i in card_nums:
            if i in winning_nums:
                card_winning_count += 1
        if card_winning_count > 0:
            card_score = 2**(card_winning_count-1)
        else:
            card_score = 0
        #print(card_score)
        total_card_score += card_score

print(total_card_score)

