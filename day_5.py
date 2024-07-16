from typing import Dict

sample_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

DAY = 5


class DestSourceRange:
    def __init__(self, dest, source, range):
        self.dest = dest
        self.source = source
        self.range = range


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


types_map: Dict[int, list[DestSourceRange]] = dict[int, list[DestSourceRange]]()
for i in range(0, 7):
    types_map[i] = []

input = get_input(False)

# Parse the input map
source_type = -1
for line in list(filter(lambda li: li != '', input.splitlines()))[1:]:
    splitted_line = line.split('-to-')
    if len(splitted_line) == 2:
        source_type += 1
    else:
        [dest, source, ds_range] = line.split(' ')
        types_map[source_type].append(DestSourceRange(int(dest), int(source), int(ds_range)))


# Range spliting
last_source_type_start_ranges = []
for source_type in reversed(range(0, 6)):
    range_numbers = (list(map(lambda m: m.dest, types_map[source_type])) +
                     list(map(lambda m: m.dest + m.range - 1, types_map[source_type])) +
                     list(map(lambda m: m.source, types_map[source_type + 1])) +
                     list(map(lambda m: m.source + m.range - 1, types_map[source_type + 1])))

    range_numbers = sorted(list(dict.fromkeys(range_numbers)))
    new_ranges = []

    for i in range(0, len(range_numbers) - 1):
        range_info = list(filter(lambda m: m.dest <= range_numbers[i] < (m.dest + m.range),
                                 types_map[source_type]))
        new_source = range_numbers[i]
        if len(range_info) == 1:
            new_source = (range_numbers[i] - range_info[0].dest) + range_info[0].source
        new_ranges.append(DestSourceRange(range_numbers[i], new_source, range_numbers[i + 1] - range_numbers[i]))
    types_map[source_type] = new_ranges

# Parse seeds part 1
seeds_part1 = list(map(lambda s_str: int(s_str), (list(input.splitlines()[0].split('seeds: ')[1].split(' ')))))

# Parse seeds part 2
seeds_ranges = []
seeds_part2 = []
for i in range(0, len(seeds_part1), 2):
    seeds_ranges.append({
        'start': int(seeds_part1[i]),
        'end': int(seeds_part1[i]) + int(seeds_part1[i + 1])
    })
    seeds_part2.append(int(seeds_part1[i]))

for i in range(0, len(types_map[0])):
    if len(list(
            filter(lambda s_r: s_r['start'] <= types_map[0][i].source < s_r['end'], seeds_ranges))) >= 1:
        seeds_part2.append(types_map[0][i].source)
seeds_part2 = sorted(list(dict.fromkeys(seeds_part2)))

# Solve part 1
part1_min_location = 1000000000
for seed in seeds_part1:
    source = int(seed)
    for source_type in range(0, 7):
        source_dest = [m for m in types_map[source_type]
                       if m.source <= source < (m.source + m.range)]

        if len(source_dest) >= 1:
            offset = source - source_dest[0].source
            source = source_dest[0].dest + offset
    part1_min_location = min(source, part1_min_location)
print(part1_min_location)

# Solve part 2
part1_min_location = 1000000000
for seed in seeds_part2:
    source = int(seed)
    for source_type in range(0, 7):
        source_dest = [m for m in types_map[source_type]
                       if m.source <= source < (m.source + m.range)]

        if len(source_dest) >= 1:
            offset = source - source_dest[0].source
            source = source_dest[0].dest + offset
    part1_min_location = min(source, part1_min_location)
print(part1_min_location)
