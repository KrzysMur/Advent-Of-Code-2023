with open("puzzle_inputs/day_3_input.txt") as file:
    lines = [line.rstrip("\n") for line in file.readlines()]


def is_symbol(char: str):
    return not char.isdigit() and char != "."


def is_adjacent_to_symbol(x: int, y: int, schematic: list[str]):
    for a, b in [[y-1, x-1], [y-1, x], [y-1, x+1]]:
        try:
            if is_symbol(schematic[a][b]):
                return True
        except IndexError:
            pass
    for a, b in [[y, x-1], [y, x+1]]:
        try:
            if is_symbol(schematic[a][b]):
                return True
        except IndexError:
            pass

    for a, b in [[y+1, x-1], [y+1, x], [y+1, x+1]]:
        try:
            if is_symbol(schematic[a][b]):
                return True
        except IndexError:
            pass

    return False


def get_adjacent_numbers(x: int, y: int, schematic: list[str]):
    adjacent_numbers = []
    top = schematic[y-1][x-3:x+4]
    bottom = schematic[y+1][x-3:x+4]
    left = schematic[y][x-3:x]
    right = schematic[y][x+1:x+4]

    if left[-1].isdigit():
        adjacent_numbers.append(int(left.split(".")[-1]))

    if right[0].isdigit():
        adjacent_numbers.append(int(right.split(".")[0]))

    top_num = top[3]
    i = 4
    while i < len(top) and top[i].isdigit():
        top_num += top[i]
        i += 1
    i = 2
    while i >= 0 and top[i].isdigit():
        top_num = top[i] + top_num
        i -= 1

    bottom_num = bottom[3]
    i = 4
    while i < len(top) and bottom[i].isdigit():
        bottom_num += bottom[i]
        i += 1
    i = 2
    while i >= 0 and bottom[i].isdigit():
        bottom_num = bottom[i] + bottom_num
        i -= 1
    return adjacent_numbers + [int(n) for n in top_num.split(".") if n] + [int(n) for n in bottom_num.split(".") if n]



def main():
    numbers_to_sum = []
    ratios_to_sum = []
    for i in range(len(lines)):
        j = 0

        while j < len(lines[0]):
            current_number = ""
            adjacent = False
            while j < len(lines[0]) and lines[i][j].isdigit():
                current_number += lines[i][j]
                if not adjacent:
                    if is_adjacent_to_symbol(j, i, lines):
                        adjacent = True
                j += 1
            if adjacent:
                numbers_to_sum.append(int(current_number))

            try:
                if lines[i][j] == "*":
                    adjacent_numbers = get_adjacent_numbers(j, i, lines)
                    if len(adjacent_numbers) == 2:
                        ratios_to_sum.append(adjacent_numbers[0] * adjacent_numbers[1])
            except IndexError:
                pass

            j += 1
    print(sum(numbers_to_sum))
    print(sum(ratios_to_sum))

main()
