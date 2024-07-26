sample_input = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""

DAY = 10


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


input = get_input(False)

two_dimension_array = list(map(lambda l: list(l), input.splitlines()))


def get_loop_length(prev_point: list[int], cur_point: list[int], stop_point: list[int]):
    length = 1
    positions = []

    while stop_point[0] != cur_point[0] or stop_point[1] != cur_point[1]:
        positions.append(cur_point)
        length += 1

        prev_x = prev_point[1]
        prev_y = prev_point[0]

        x = cur_point[1]
        y = cur_point[0]

        prev_point = cur_point
        if two_dimension_array[y][x] == '-':
            if prev_x < x:
                cur_point = [y, x + 1]
            else:
                cur_point = [y, x - 1]
        elif two_dimension_array[y][x] == '|':
            if prev_y < y:
                cur_point = [y + 1, x]
            else:
                cur_point = [y - 1, x]
        elif two_dimension_array[y][x] == 'L':
            if prev_y < y:
                cur_point = [y, x + 1]
            else:
                cur_point = [y - 1, x]
        elif two_dimension_array[y][x] == 'J':
            if prev_y < y:
                cur_point = [y, x - 1]
            else:
                cur_point = [y - 1, x]
        elif two_dimension_array[y][x] == 'F':
            if prev_x > x:
                cur_point = [y + 1, x]
            else:
                cur_point = [y, x + 1]
        elif two_dimension_array[y][x] == '7':
            if prev_x < x:
                cur_point = [y + 1, x]
            else:
                cur_point = [y, x - 1]
        else:
            break

    return (length, positions)


start_point = []
for y in range(0, len(two_dimension_array)):
    for x in range(0, len(two_dimension_array[y])):
        if two_dimension_array[y][x] == 'S':
            start_point = [y, x]
            break

farthest_in_loop_length = 0
farthest_in_loop_positions = []

if start_point[1] > 0:
    (length, positions) = get_loop_length(start_point, [start_point[0], start_point[1] - 1], start_point)
    if length > farthest_in_loop_length:
        farthest_in_loop_length = length
        farthest_in_loop_positions = positions

if start_point[0] > 0:
    (length, positions) = get_loop_length(start_point, [start_point[0] - 1, start_point[1]], start_point)
    if length > farthest_in_loop_length:
        farthest_in_loop_length = length
        farthest_in_loop_positions = positions

if start_point[0] < (len(two_dimension_array) - 1):
    (length, positions) = get_loop_length(start_point, [start_point[0] + 1, start_point[1]], start_point)
    if length > farthest_in_loop_length:
        farthest_in_loop_length = length
        farthest_in_loop_positions = positions

if start_point[1] < (len(two_dimension_array[0]) - 1):
    (length, positions) = get_loop_length(start_point, [start_point[0], start_point[1] + 1], start_point)
    if length > farthest_in_loop_length:
        farthest_in_loop_length = length
        farthest_in_loop_positions = positions

part1 = farthest_in_loop_length / 2
print(part1)

farthest_in_loop_positions.append(start_point)

farthest_in_loop_positions_set = set(map(lambda p: f'{p[0]}_{p[1]}', farthest_in_loop_positions))

# Clean non loop items
for y in range(0, len(two_dimension_array)):
    for x in range(0, len(two_dimension_array[y])):
        if f'{y}_{x}' not in farthest_in_loop_positions_set:
            two_dimension_array[y][x] = '.'

index_of_start = farthest_in_loop_positions.index(start_point)

index_before = 0 if index_of_start + 1 == len(farthest_in_loop_positions) else index_of_start + 1
index_after = 0 if index_of_start == 0 else index_of_start - 1

before = two_dimension_array[farthest_in_loop_positions[index_before][0]][farthest_in_loop_positions[index_before][1]]
after = two_dimension_array[farthest_in_loop_positions[index_after][0]][farthest_in_loop_positions[index_after][1]]

# Replace the starting point value with the relevant symbol. It's needed for calculating the inside count.
if (before == '-' and after == '|') or (after == '-' and before == '|'):
    diff_y = farthest_in_loop_positions[index_before][1] - farthest_in_loop_positions[index_after][1]
    diff_x = farthest_in_loop_positions[index_before][0] - farthest_in_loop_positions[index_after][0]

    if before == '-':
        if diff_y == 1 and diff_x == 1:
            two_dimension_array[start_point[0]][start_point[1]] = '7'
        elif diff_y == -1 and diff_x == 1:
            two_dimension_array[start_point[0]][start_point[1]] = 'J'
        elif diff_y == 1 and diff_x == -1:
            two_dimension_array[start_point[0]][start_point[1]] = 'F'
        elif diff_y == -1 and diff_x == -1:
            two_dimension_array[start_point[0]][start_point[1]] = 'L'
    elif before == '|':
        if diff_y == 1 and diff_x == 1:
            two_dimension_array[start_point[0]][start_point[1]] = 'L'
        elif diff_y == -1 and diff_x == 1:
            two_dimension_array[start_point[0]][start_point[1]] = 'F'
        elif diff_y == 1 and diff_x == -1:
            two_dimension_array[start_point[0]][start_point[1]] = 'J'
        elif diff_y == -1 and diff_x == -1:
            two_dimension_array[start_point[0]][start_point[1]] = '7'
elif before == '-' or after == '-':
    two_dimension_array[start_point[0]][start_point[1]] = '-'
else:
    two_dimension_array[start_point[0]][start_point[1]] = '|'

part2_count_inside = 0
for y in range(0, len(two_dimension_array)):
    is_inside = False
    last_seperator = '|'
    for x in range(0, len(two_dimension_array[y])):
        if two_dimension_array[y][x] == '|':
            is_inside = not is_inside
        elif two_dimension_array[y][x] != '-' and two_dimension_array[y][x] != '.':
            if last_seperator != '|':
                if not ((last_seperator == 'F' and two_dimension_array[y][x] == '7') or
                        (last_seperator == 'L' and two_dimension_array[y][x] == 'J')):
                    is_inside = not is_inside
                last_seperator = '|'
            else:
                last_seperator = two_dimension_array[y][x]

        if two_dimension_array[y][x] == '.':
            if is_inside:
                two_dimension_array[y][x] = 'I'
                part2_count_inside += 1
            else:
                two_dimension_array[y][x] = 'O'

print(part2_count_inside)
