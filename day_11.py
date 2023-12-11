with open("puzzle_inputs/day_11_input.txt") as file:
    lines = [list(line.rstrip("\n")) for line in file.readlines()]
EXPANSION_RATE = 1000000


def main():
    galaxies = get_galaxies_coordinates()
    total = 0

    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            total += get_distance(galaxies[i], galaxies[j])
    print(total)


def get_distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def get_galaxies_coordinates():
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                x = j + count_empty_columns_before(j) * (EXPANSION_RATE - 1)
                y = i + count_empty_rows_before(i) * (EXPANSION_RATE - 1)
                galaxies.append([x, y])
    return galaxies


def count_empty_columns_before(j):
    counter = 0
    for i in range(j):
        col = [line[i] for line in lines]
        if "#" not in col:
            counter += 1
    return counter


def count_empty_rows_before(i):
    counter = 0
    for row in lines[:i]:
        if "#" not in row:
            counter += 1
    return counter


main()
