import math

sample_input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

DAY = 13

USE_SAMPLE = False

# Parse input
record_to_arrangments_count = dict()
day_input = sample_input if USE_SAMPLE else open(f'day_{DAY}_input.txt', "r").read()


def parse_input():
    patterns = []
    pattern = []

    # empty row because we add a pattern when reaching an empty row
    input_lines = day_input.splitlines()
    for line_i in range(0, len(input_lines)):
        row = input_lines[line_i]
        if row == "" or line_i == len(input_lines) - 1:
            if line_i == len(input_lines) - 1:
                pattern.append(row)
            rows = [str(row_a) for row_a in pattern]
            cols = ["".join([row[col_i] for row in pattern]) for col_i in range(0, len(pattern[0]))]
            patterns.append({"rows": rows, "columns": cols})
            pattern = []
        else:
            pattern.append(row)

    return patterns


def get_smudges_count(element1, element2):
    smudges = 0
    for i in range(0, len(element1)):
        if element1[i] != element2[i]:
            smudges += 1
    return smudges


def is_reflection(index, elements: list[str], part):
    elements_above_count = index + 1
    elements_below_count = len(elements) - index - 1
    elements_to_iterate = min(elements_above_count, elements_below_count)

    if elements_to_iterate <= 0:
        return False

    i_first = index
    i_second = index + 1

    smudges = 0
    for i in range(0, elements_to_iterate):
        smudges += get_smudges_count(elements[i_first], elements[i_second])
        i_first -= 1
        i_second += 1

    return smudges == 0 if part == 1 else smudges == 1


def get_reflection_sum(elements, part, multiplyby=1):
    sum = 0
    elements_middle_i = math.ceil(len(elements) / 2)
    elements_indexes = (list(reversed([index for index in range(0, elements_middle_i + 1)])) +
                        list([index for index in range(elements_middle_i + 1, len(elements))]))
    elements_indexes.sort(reverse=True)
    for i in elements_indexes:
        if is_reflection(i, elements, part):
            sum += multiplyby * (i + 1)
            break

    return sum


def solve1():
    patterns = parse_input()
    print(sum(list([(get_reflection_sum(pattern["rows"], 1, multiplyby=100) +
                     get_reflection_sum(pattern["columns"], 1)) for pattern in patterns])))


def solve2():
    patterns = parse_input()
    print(sum(list([(get_reflection_sum(pattern["rows"], 2, multiplyby=100) +
                     get_reflection_sum(pattern["columns"], 2)) for pattern in patterns])))


solve1()
solve2()
