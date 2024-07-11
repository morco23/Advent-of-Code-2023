sample_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

DAY = 4


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


input = get_input(False)


def get_winning_chosen_numbers_count(winning, chosen):
    winning_set = dict()
    for win_number in winning:
        winning_set[win_number] = True

    chosen_hits = 0
    for number in chosen:
        if number in winning_set:
            chosen_hits += 1

    return chosen_hits


def get_score(hits):
    if hits <= 2:
        return hits
    else:
        return pow(2, hits - 1)


part1_sum = 0
card_to_duplicate_count = dict()
card_num = 1
part2_card_counts = 0

for line in input.splitlines():
    # Remove 'Card X: '
    line = line[line.index(': ') + 2:]

    winning_numbers, chosen_numbers = list(map(lambda line_part: list(filter(lambda n: n != '',
                                                                             line_part.split(' '))),
                                               line.split('|')))

    hits = get_winning_chosen_numbers_count(winning_numbers, chosen_numbers)
    part1_sum += get_score(hits)

    if card_num not in card_to_duplicate_count:
        card_to_duplicate_count[card_num] = 1
    else:
        card_to_duplicate_count[card_num] += 1

    for card_num_to_add_duplicate in range(card_num + 1, hits + card_num + 1):
        if card_num_to_add_duplicate not in card_to_duplicate_count:
            card_to_duplicate_count[card_num_to_add_duplicate] = 0
        card_to_duplicate_count[card_num_to_add_duplicate] += card_to_duplicate_count[card_num]

    card_num += 1

print(part1_sum)

part2_card_counts = sum(list(card_to_duplicate_count.values()))
print(part2_card_counts)
