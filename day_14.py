with open("puzzle_inputs/day_14_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


def main():
    move_rocks()
    total_load = get_total_load()
    print(total_load)


def move_rocks():
    for i in range(1, len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "O":
                roll_rock(i, j)


def roll_rock(i, j):
    while i > 0 and lines[i-1][j] == ".":
        replace(i, j, ".")
        i -= 1
        replace(i, j, "O")


def replace(i, j, char):
    lines[i] = lines[i][:j] + char + lines[i][j+1:]


def get_total_load():
    total_load = 0
    for i in range(1, len(lines)+1):
        total_load += i * lines[-i].count("O")
    return total_load


main()
