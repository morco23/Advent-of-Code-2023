from math import gcd

DAY = 8

sample_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


input = get_input(False)
lines = input.splitlines()

directions = list(input.splitlines()[0])

label_to_right_left = dict()

for line in lines[2:]:
    line_parts = line.replace("(", "").replace(")", "").replace(",", "").split(" ")
    label_to_right_left[line_parts[0]] = {
        "L": line_parts[2],
        "R": line_parts[3]
    }

part_1_steps_count = 0
cur = 'AAA'
while cur != 'ZZZ':
    for direction in directions:
        cur = label_to_right_left[cur][direction]
        part_1_steps_count += 1
        if cur == 'ZZZ':
            break

labels_end_with_a = [label for label in label_to_right_left.keys() if label.endswith('A')]
labels_end_with_a_all_steps_counts = []
for label in labels_end_with_a:
    cur = label
    steps_count = 0
    while not cur.endswith('Z'):
        for direction in directions:
            cur = label_to_right_left[cur][direction]
            steps_count += 1
            if cur.endswith('Z'):
                labels_end_with_a_all_steps_counts.append(steps_count)
                break


def calculate_lcm(counts):
    lcm = 1
    for i in counts:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


part_2_steps_count = calculate_lcm(labels_end_with_a_all_steps_counts)
print(part_2_steps_count)
