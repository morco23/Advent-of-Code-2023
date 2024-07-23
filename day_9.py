sample_input = """10 13 16 21 30 45"""

DAY = 9


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


input = get_input(False)

history_array = []
for line in input.splitlines():
    history_array.append([int(history) for history in line.split(' ')])


def get_extrapolated_value_rec(history: list[int], extrapolate_prev = False):
    differences = []
    all_zero = True

    for i in range(0, len(history) - 1):
        difference = history[i + 1] - history[i]

        if difference != 0:
            all_zero = False

        differences.append(difference)

    next_diffrence = 0
    if not all_zero:
        next_diffrence = get_extrapolated_value_rec(differences, extrapolate_prev)

    if extrapolate_prev:
        return history[0] - next_diffrence
    else:
        return history[-1] + next_diffrence


part_1_sum = sum(get_extrapolated_value_rec(history) for history in history_array)
print(part_1_sum)

part_2_sum = sum(get_extrapolated_value_rec(history, True) for history in history_array)
print(part_2_sum)