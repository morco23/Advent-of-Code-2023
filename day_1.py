import re

sample_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

DAY = 1


def get_input(sample):
    if sample:
        return sample_input
    return open(f'day_{DAY}_input.txt', "r").read()


number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}


# Function to replace number words with digits
def replace_number_words(text):
    for number_str in number_dict:
        # Add the number_str to the beginning and end to handle overlapping.
        text = re.compile(number_str).sub(number_str + number_dict[number_str] + number_str, text)

    return re.compile('[a-zA-Z]').sub('', text)


day_input = get_input(False)

lines = day_input.splitlines()

# Part 1:
count = 0
for line in lines:
    line = re.compile('[a-zA-Z]').sub('', line)
    count += int(line[0] + line[-1])
print(count)

# Part 2:
count = 0
for line in lines:
    line = replace_number_words(line)
    count += int(line[0] + line[-1])

print(count)
