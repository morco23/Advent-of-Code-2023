from typing import Dict

sample_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

DAY = 7

card_labels = ['Joker', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


hands_bids = []
for line in get_input(False).splitlines():
    [hand, bid] = line.split((" "))
    hands_bids.append({
        'hand': hand,
        'replaced_jokers': hand,
        'bid': int(bid)
    })


def replace_jokers_in_hands(hands_bids):
    for hand_bid in hands_bids:
        hand = list(hand_bid['hand'])
        if 'J' in hand:
            j_indexes = []
            label_to_count = dict()
            for i in range(0, len(hand)):
                label = hand[i]
                if label == 'J':
                    j_indexes.append(i)
                else:
                    if label_to_count.get(label) is None:
                        label_to_count[label] = 0
                    label_to_count[label] += 1

            labels = list(label_to_count.keys())
            label_instead_joker = 'A'
            if len(labels) >= 1:
                labels.sort(
                    key=lambda l_c_k: label_to_count[l_c_k] * 100 + card_labels.index(l_c_k), reverse=True)
                label_instead_joker = labels[0]

            for j_index in j_indexes:
                hand[j_index] = label_instead_joker

            hand_bid['replaced_jokers'] = ''.join(hand)


def get_hand_score(hand, replaced_jokers_hand, joker_enable):

    label_to_count = dict()
    cards_score = 0
    type_score = 0

    hand_list = list(hand)
    for i in range(0, len(hand_list)):
        label = hand_list[i]
        array_index = 1 if joker_enable and label == 'J' else card_labels.index(label) + 1
        cards_score += array_index
        cards_score *= 100
    cards_score /= 100

    hand_list = list(replaced_jokers_hand)
    for i in range(0, len(hand_list)):
        label = hand_list[i]
        if label_to_count.get(label) is None:
            label_to_count[label] = 0
        label_to_count[label] += 1

    distincted_hand_labels = list(set(label_to_count))

    if len(list(filter(lambda l: label_to_count[l] == 5, distincted_hand_labels))) == 1:
        type_score = 70000000000
    elif len(list(filter(lambda l: label_to_count[l] == 4, distincted_hand_labels))) == 1:
        type_score = 60000000000
    elif len(list(filter(lambda l: label_to_count[l] == 3, distincted_hand_labels))) == 1:
        if len(list(filter(lambda l: label_to_count[l] == 2, distincted_hand_labels))) == 1:
            type_score = 50000000000
        else:
            type_score = 40000000000
    elif len(list(filter(lambda l: label_to_count[l] == 2, distincted_hand_labels))) == 2:
        type_score = 20000000000
    elif len(list(filter(lambda l: label_to_count[l] == 2, distincted_hand_labels))) == 1:
        type_score = 10000000000

    return type_score + cards_score


rank_parts1 = 0
hands_bids.sort(key=lambda h_b: get_hand_score(h_b['hand'], h_b['replaced_jokers'], False))
for i in range(len(hands_bids)):
    rank_parts1 += (i + 1) * hands_bids[i]["bid"]

print(rank_parts1)

rank_parts2 = 0
replace_jokers_in_hands(hands_bids)
hands_bids.sort(key=lambda h_b: get_hand_score(h_b['hand'], h_b['replaced_jokers'], True))
for i in range(len(hands_bids)):
    rank_parts2 += (i + 1) * hands_bids[i]["bid"]

print(rank_parts2)
