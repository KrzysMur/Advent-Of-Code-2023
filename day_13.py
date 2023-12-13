with open("puzzle_inputs/day_13_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

patterns = []
current_pattern = []
for line in lines:
    if line:
        current_pattern.append(line)
    else:
        patterns.append(current_pattern)
        current_pattern = []
patterns.append(current_pattern)



def main():
    total = 0
    for pattern in patterns:
        vertical_reflection = find_vertical_reflection(pattern)
        horizontal_reflection = find_horizontal_reflection(pattern)

        total += vertical_reflection + 100 * horizontal_reflection

    print(total)


def find_vertical_reflection(pattern):
    vertical_reflections = []
    for i in range(1, len(pattern[0])):
        for line in pattern:
            is_ref = is_reflection(line[:i], line[i:])
            if not is_ref:
                break
        else:
            vertical_reflections.append(i)
    return sum(vertical_reflections)


def is_reflection(string1, string2):
    length_diff = len(string1) - len(string2)
    if length_diff >= 0:
        string1 = "".join(reversed(string1[length_diff:]))
    else:
        string2 = "".join(reversed(string2[:length_diff]))
    return string2 == string1


def find_horizontal_reflection(pattern):
    horizontal_reflections = []
    for i in range(1, len(pattern)):
        top_half, bottom_half = pattern[:i], pattern[i:]
        length_diff = len(bottom_half) - len(top_half)
        if length_diff > 0:
            bottom_half = list(reversed(bottom_half[:-length_diff]))
        else:
            top_half = list(reversed(top_half[-length_diff:]))

        if top_half == bottom_half:
            horizontal_reflections.append(i)
    return sum(horizontal_reflections)


main()
