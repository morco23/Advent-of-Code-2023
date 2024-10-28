from typing import Union

sample_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

DAY = 12

USE_SAMPLE = False

# Parse input
record_to_arrangments_count = dict()
day_input = sample_input if USE_SAMPLE else open(f'day_{DAY}_input.txt', "r").read()


def parse_input(part: int):
    cr = []
    for row in day_input.splitlines():
        [format1_str, format2_str] = row.split(' ')
        format1 = [symbol for symbol in format1_str]
        format2 = [int(number) for number in format2_str.split(',')]

        if part == 2:
            extended_format_1 = []
            extended_format_2 = []
            extended_format_1.extend(format1)
            extended_format_2.extend(format2)

            for _ in range(4):
                extended_format_1.append('?')
                extended_format_1.extend(format1)
                extended_format_2.extend(format2)

            format1 = extended_format_1
            format2 = extended_format_2

        cr.append({'format1': format1, 'format2': format2})
    return cr


def convert_to_format2(format1: list):
    format2 = []
    group_size = 0
    for symbol in format1:
        if symbol == '.' or symbol == '?':
            if group_size > 0:
                format2.append(group_size)
                group_size = 0
        else:
            group_size += 1
    if group_size > 0:
        format2.append(group_size)

    return format2


def get_first_group(format1: list):
    group_size = 0
    group_start_index = 0
    for symbol in format1:
        if symbol == '?':
            return 0, 0
        if symbol == '.' and group_size > 0:
            return group_start_index, group_size
        if symbol == '#':
            group_size += 1
        else:
            group_start_index += 1

    return group_start_index, group_size


def get_record_key(record):
    return str(record['format1']) + str(record['format2'])


def get_arrangements_count(record: dict[str, Union[list[int], list]]):
    record_key = get_record_key(record)

    if record_key in record_to_arrangments_count:
        return record_to_arrangments_count[record_key]
    group_start_index, group_size = get_first_group(record['format1'])

    arrangment_count = 0
    format1_only_dots_or_empty = all(element == '.' for element in record['format1']) or len(record['format1']) == 0
    format1_any_active_symbol = any(element == '#' for element in record['format1']) and len(record['format1']) > 0

    if len(record['format2']) == 0 and format1_only_dots_or_empty:
        arrangment_count = 1
    elif len(record['format2']) == 0 and format1_any_active_symbol:
        arrangment_count = 0
    else:
        if 0 < group_size:
            if group_size != record['format2'][0]:
                arrangment_count = 0
            else:
                arrangment_count = get_arrangements_count(
                    {'format1': record['format1'][group_start_index + group_size:],
                     'format2': record['format2'][1:]})
        else:
            indexes_q = [index for index, value in enumerate(record['format1']) if value == '?']
            if len(indexes_q) > 0:
                format1_next1: list = record['format1'][:]
                format1_next1[indexes_q[0]] = '.'
                format1_next2: list = record['format1'][:]
                format1_next2[indexes_q[0]] = '#'
                arrangment_count = (get_arrangements_count({'format1': format1_next1,
                                                            'format2': record['format2']}) +
                                    get_arrangements_count({'format1': format1_next2,
                                                            'format2': record['format2']}))
        record_key = get_record_key(record)
        record_to_arrangments_count[record_key] = arrangment_count

    return arrangment_count


def solve(part: int):
    condition_records = parse_input(part)
    arrangements_sum = 0
    record_index = 0
    for record in condition_records:
        arrangements_sum += get_arrangements_count(record)
        record_index += 1
        if record_index % 10 == 0:
            print(f'{record_index}/{len(condition_records)}')
    print(arrangements_sum)

solve(1)
solve(2)