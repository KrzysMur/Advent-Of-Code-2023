with open("puzzle_inputs/day_11_input.txt") as file:
    lines = [list(line.rstrip("\n")) for line in file.readlines()]


def main():
    expand_columns()
    expand_rows()
    galaxies = get_galaxies_coordinates()
    total = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            total += get_distance(galaxy1, galaxy2)
    print(total//2)


def get_distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def get_galaxies_coordinates():
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                galaxies.append((j, i))
    return galaxies


def expand_rows():
    i = 0
    while i < len(lines):
        if "#" not in lines[i]:
            lines.insert(i, lines[i])
            i += 1
        i += 1


def expand_columns():
    i = 0
    while i < len(lines[0]):
        column = [line[i] for line in lines]
        if "#" not in column:
            for j in range(len(lines)):
                lines[j].insert(i, ".")
            i += 1
        i += 1


main()
