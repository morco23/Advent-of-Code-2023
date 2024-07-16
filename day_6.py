from typing import Dict

sample_input = """Time:      7  15   30
Distance:  9  40  200"""

DAY = 6


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


times_part1 = []
distances_part1 = []
for line in get_input(False).splitlines():
    if line.startswith("Time:"):
        times_part1 = [int(t.strip()) for t in line.replace("Time:", "").split(' ') if t.strip() != '']

    if line.startswith("Distance:"):
        distances_part1 = [int(d.strip()) for d in line.replace("Distance:", "").split(' ') if d.strip() != '']

time_part2 = []
distance_part2 = []
for line in get_input(False).splitlines():
    if line.startswith("Time:"):
        time_part2 = int(line.replace("Time:", "").replace(" ", ""))

    if line.startswith("Distance:"):
        distance_part2 = int(line.replace("Distance:", "").replace(" ", ""))


def get_margin(max_ms, distance):
    best_holding = int(max_ms / 2)
    margin = 0

    if (best_holding * (max_ms - best_holding)) > distance:
        margin += (1 if max_ms % 2 == 0 else 2)

    for i in reversed(range(0, best_holding)):
        score = i * (max_ms - i)
        if score > distance:
            margin += 2
        else:
            return margin
    return margin


margin_multiplied_part1 = 1
for i in range(0, len(times_part1)):
    margin = get_margin(times_part1[i], distances_part1[i])
    margin_multiplied_part1 *= margin
print(margin_multiplied_part1)

part2_margin = get_margin(time_part2, distance_part2)
print(part2_margin)
