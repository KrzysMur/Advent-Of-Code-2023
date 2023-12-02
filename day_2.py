BAG_CONTENT = {"green": 13, "red": 12, "blue": 14}


def main():

    with open("puzzle_inputs/day_2_input.txt") as file:
        games = [line.rstrip("\n").split(":")[1].split(";") for line in file.readlines()]

    total_possible = 0
    total_powers = 0
    i = 1
    for game in games:
        if is_game_possible(game):
            total_possible += i
        total_powers += get_power_of_game(game)
        i += 1
    print(total_possible, total_powers)


def is_game_possible(game):
    for subset in game:
        if not is_subset_possible(subset):
            return False
    return True


def is_subset_possible(subset: str):
    for color in subset.split(", "):
        split_color = color.split()
        if int(split_color[0]) > BAG_CONTENT[split_color[1]]:
            return False
    return True


def find_minimum_required_cubes(game):
    maximum = {"green": 0, "red": 0, "blue": 0}
    for subset in game:
        for color in subset.split(", "):
            color_split = color.split()
            if int(color_split[0]) > maximum[color_split[1]]:
                maximum.update({color_split[1]: int(color_split[0])})
    return maximum


def get_power_of_game(game):
    power = 1
    for value in find_minimum_required_cubes(game).values():
        power *= value
    return power


main()
