
DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("puzzle_inputs/day_1_input.txt") as file:
    puzzle_input = [line.rstrip("\n") for line in file.readlines()]


def is_digit(char):
    return 48 <= ord(char) <= 57


def find_first_digit(line):
    for i in range(len(line)):
        if is_digit(line[i]):
            return line[i]

        for digit in DIGITS.keys():
            if line[i:].startswith(digit):
                return DIGITS[digit]


def find_last_digit(line):
    for i in range(len(line)-1, -1, -1):
        if is_digit(line[i]):
            return line[i]

        for digit in DIGITS.keys():
            if line[:i+1].endswith(digit):
                return str(DIGITS[digit])


def get_calibration_value(line):
    return int(find_first_digit(line) + find_last_digit(line))


def sum_calibration_values(lines):
    total = 0
    for line in lines:
        total += get_calibration_value(line)
    return total


print(sum_calibration_values(puzzle_input))
