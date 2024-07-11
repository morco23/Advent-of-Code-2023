import re

sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

DAY = 3


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


day_input = get_input(False)
day_input_lines = day_input.splitlines()

# Create two-dimensional array to holds the input
rows_count, cols_count = len(day_input_lines), len(day_input_lines[0])
two_dim_array = [['.' for _ in range(rows_count)] for _ in range(cols_count)]

# Populate the array with the input
for row_i in range(0, rows_count):
    for col_i in range(0, cols_count):
        two_dim_array[row_i][col_i] = day_input_lines[row_i][col_i]


# Ensure that the indices are within the valid range of the array.
def is_valid(row_i, col_i):
    return 0 <= row_i < rows_count and 0 <= col_i < cols_count


def get_surrounding_indices(row_i, col_i):
    return [(row_i, col_i + 1), (row_i + 1, col_i), (row_i + 1, col_i + 1),
            (row_i - 1, col_i), (row_i, col_i - 1), (row_i - 1, col_i - 1),
            (row_i - 1, col_i + 1), (row_i + 1, col_i - 1)]


def et_surrounding_symbols(row_i, col_i):
    surrounding_symbols = filter(lambda row_col: is_valid(row_col[0], row_col[1]),
                                 get_surrounding_indices(row_i, col_i))
    surrounding_symbols = filter(lambda row_col: not two_dim_array[row_col[0]][row_col[1]].isdigit() and
                                                 two_dim_array[row_col[0]][row_col[1]] != '.', surrounding_symbols)
    return list(surrounding_symbols)


# Array of tupel of number and the surrounding_symbols
numbers_to_symbols = []
part1_sum = 0

number_str = ''

symbols = []

gear_symbols = []

part2_sum = 0

for row_i in range(0, rows_count):
    for col_i in range(0, cols_count):
        if two_dim_array[row_i][col_i].isdigit():
            number_str += two_dim_array[row_i][col_i]

            for symbol in et_surrounding_symbols(row_i, col_i):
                symbols.append(symbol)
        else:
            if two_dim_array[row_i][col_i] == '*':
                gear_symbols.append((row_i, col_i))
            if number_str != '':
                if len(symbols):
                    part1_sum += int(number_str)
                    numbers_to_symbols.append({'number': number_str, 'symbols': symbols})
                    symbols = []
                number_str = ''

for gear_symbol in gear_symbols:
    # Filter numbers to symbols where there is any '*' symbol at the same position as gear_symbol
    filtered_number_to_symbols = list(filter(lambda n_s: n_s['symbols'].count(gear_symbol) > 0, numbers_to_symbols))
    filtered_number = list(map(lambda n_s: n_s['number'], filtered_number_to_symbols))
    if len(filtered_number) == 2:
        part2_sum += int(filtered_number[0]) * int(filtered_number[1])

print(part1_sum)
print(part2_sum)
