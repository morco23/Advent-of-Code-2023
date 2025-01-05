sample_input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

DAY = 15

USE_SAMPLE = False

# Parse input
day_input = sample_input if USE_SAMPLE else open(f'day_{DAY}_input.txt', "r").read()


def parse_input():
    input_lines = day_input.replace(',', '\n')
    return input_lines.splitlines()


def get_hash(step):
    hash_value = 0
    for ch in step:
        hash_value += ord(ch)
        hash_value *= 17
        hash_value %= 256
    return hash_value


def solve1():
    init_seq = parse_input()
    hash_sum = sum([get_hash(step) for step in init_seq])
    print(hash_sum)


def solve2():
    init_seq = parse_input()
    boxes = dict()
    for step in init_seq:
        if '-' in step:
            step_parts = step.split('-')
            operation = 'del'
        else:
            step_parts = step.split('=')
            operation = 'add'

        box_num = get_hash(step_parts[0])
        if get_hash(step_parts[0]) not in boxes:
            boxes[box_num] = []

        if operation == 'del':
            boxes[box_num] = [lens for lens in boxes[box_num] if not lens.startswith(f'{step_parts[0]}=')]
        else:
            matches = [index for index, lens in enumerate(boxes[box_num]) if lens.startswith(f'{step_parts[0]}=')]
            if len(matches) == 0:
                boxes[box_num].append(step)
            else:
                boxes[box_num][matches[0]] = step

    focusing_power = (
        sum(
            [sum(
                [(box + 1) * (index + 1) * int(lens.split('=')[1]) for index, lens in enumerate(boxes[box])])
                for box in boxes]))
    print(focusing_power)


solve1()
solve2()