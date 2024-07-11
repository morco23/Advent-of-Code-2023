import re

sample_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

DAY = 2


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


day_input = get_input(False)

config_red = 12
config_green = 13
config_blue = 14

part1_count = 0
part2_count = 0

for line in day_input.splitlines():
    red = max(map(lambda num_str: int(num_str), re.compile('(\d+)(?=\s*red)').findall(line)))
    blue = max(map(lambda num_str: int(num_str), re.compile('(\d+)(?=\s*blue)').findall(line)))
    green = max(map(lambda num_str: int(num_str), re.compile('(\d+)(?=\s*green)').findall(line)))

    if red <= config_red and blue <= config_blue and green <= config_green:
        part1_count += int(re.compile(r'(?<=Game )[\d]+').search(line)[0])

    part2_count += (red * blue * green)

print(part1_count)
print(part2_count)
