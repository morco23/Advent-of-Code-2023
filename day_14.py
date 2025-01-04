sample_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

DAY = 14

USE_SAMPLE = False

# Parse input
day_input = sample_input if USE_SAMPLE else open(f'day_{DAY}_input.txt', "r").read()

def parse_input():
    input_lines = day_input.splitlines()
    platform = [ [pos for pos in line] for line in input_lines]
    return platform

def tilt_top(platform):
    position_changed = True
    while position_changed:
        position_changed = False
        for col_index in range(0, len(platform[0])):
            for row_index in range(1, len(platform)):
                if (platform[row_index][col_index] == 'O' and
                    platform[row_index - 1][col_index] == '.'):
                        platform[row_index][col_index] = '.'
                        platform[row_index - 1][col_index] = 'O'
                        position_changed = True

def tilt_right(platform):
    position_changed = True
    while position_changed:
        position_changed = False
        for col_index in reversed(range(0, len(platform[0]) - 1)):
            for row_index in range(0, len(platform)):
                if (platform[row_index][col_index] == 'O' and
                    platform[row_index][col_index + 1] == '.'):
                        platform[row_index][col_index] = '.'
                        platform[row_index][col_index + 1] = 'O'
                        position_changed = True

def tilt_left(platform):
    position_changed = True
    while position_changed:
        position_changed = False
        for col_index in range(1, len(platform[0])):
            for row_index in range(0, len(platform)):
                if (platform[row_index][col_index] == 'O' and
                    platform[row_index][col_index -1] == '.'):
                        platform[row_index][col_index] = '.'
                        platform[row_index][col_index - 1] = 'O'
                        position_changed = True

def tilt_bottom(platform):
    position_changed = True
    while position_changed:
        position_changed = False
        for col_index in range(0, len(platform[0])):
            for row_index in reversed(range(0, len(platform) - 1)):
                if (platform[row_index][col_index] == 'O' and
                    platform[row_index + 1][col_index] == '.'):
                        platform[row_index][col_index] = '.'
                        platform[row_index + 1][col_index] = 'O'
                        position_changed = True

def print_platform(platform):
    for row_index in range(0, len(platform)):
        print(platform[row_index])

def calculate_total_load_top_beams(platform):
    total = 0
    for col_index in range(0, len(platform[0])):
        for row_index in range(0, len(platform)):
            if platform[row_index][col_index] == 'O':
                total += len(platform) - row_index
    return total

def solve1():
    platform_input = parse_input()
    tilt_top(platform_input)
    print(f'Part1: {calculate_total_load_top_beams(platform_input)}')

def solve2():
    platform_input = parse_input()
    pattern_store = dict()
    spins_to_count = dict()
    spins = 1000000000

    # We want to recognize a sample so we start run and stop when there are enough data to work with
    spin = 0
    max_items_in_pattern = 0
    while max_items_in_pattern < 5:
        tilt_top(platform_input)
        tilt_left(platform_input)
        tilt_bottom(platform_input)
        tilt_right(platform_input)
        state = ''.join([''.join(row) for row in platform_input])
        if state not in pattern_store:
            pattern_store[state] = []
            spins_to_count[state] = calculate_total_load_top_beams(platform_input)
        pattern_store[state].append(spin + 1)
        spin += 1
        max_items_in_pattern = max(max_items_in_pattern, len(pattern_store[state]))

    # Use the pattern store to find which of them fit the number of spins we have asked to run.
    for pattern in pattern_store:
        spin_iterations = pattern_store[pattern]
        if len(spin_iterations) > 2 and (spins - spin_iterations[-2]) % (
                spin_iterations[-1] - spin_iterations[-2]) == 0:
            print(f'Part2: {spins_to_count[pattern]}')
            break

solve1()
solve2()
