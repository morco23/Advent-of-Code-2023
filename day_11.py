from itertools import combinations

sample_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

DAY = 11


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


input = get_input(False)

observatory_data = list(map(lambda l: list(l), input.splitlines()))

galaxy_id_to_index = dict()
galaxy_id = 1
for y, row in enumerate(observatory_data):
    for x, element in enumerate(row):
        if element == '#':
            observatory_data[y][x] = galaxy_id
            galaxy_id_to_index[galaxy_id] = [y, x]
            galaxy_id += 1

empty_rows = [y_index for y_index in range(0, len(observatory_data)) if len(list(filter(lambda x: x != '.',
                                                                                        observatory_data[
                                                                                            y_index]))) == 0]

empty_cols = [x_index for x_index in range(0, len(observatory_data[0])) if len(list(filter(
    lambda row: row[x_index] != '.',
    observatory_data))) == 0]


def get_distance(source_value, dest_value, expansion_multiplier=1):
    source_index = galaxy_id_to_index[source_value]
    dest_index = galaxy_id_to_index[dest_value]

    expansion_rows = len(
        [y for y in empty_rows if source_index[0] >= y >= dest_index[0] or dest_index[0] >= y >= source_index[0]])
    expansion_cols = len(
        [x for x in empty_cols if source_index[1] >= x >= dest_index[1] or dest_index[1] >= x >= source_index[1]])

    return (abs(source_index[0] - dest_index[0]) + abs(source_index[1] - dest_index[1]) + (
            expansion_rows * expansion_multiplier) +
            (expansion_cols * expansion_multiplier))


all_pairs = list(combinations(list(set([element for row in observatory_data for element in row if element != '.'])), 2))

part1_distances_sum = sum([get_distance(pair[0], pair[1]) for pair in all_pairs])

print(part1_distances_sum)

part2_distances_sum = sum([get_distance(pair[0], pair[1], 1000000 - 1) for pair in all_pairs])

print(part2_distances_sum)
