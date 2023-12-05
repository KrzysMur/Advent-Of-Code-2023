with open("puzzle_inputs/day_5_input.txt") as file:
    almanac = [line.rstrip("\n") for line in file.readlines() if line != "\n"]


def main():
    seeds = [int(seed) for seed in almanac.pop(0)[6:].split()]
    for i in range(len(seeds)):
        seeds[i] = get_final_destination(seeds[i])
    print(min(seeds))


def get_destination(source, maps):
    for number_map in maps:
        if number_map[1] <= source < number_map[1] + number_map[2]:
            return source + number_map[0] - number_map[1]
    return source


def get_final_destination(source):
    maps_list = read_maps()
    for maps in maps_list:
        source = get_destination(source, maps)
    return source


def read_maps():
    maps = []
    new_map = []
    for line in almanac[1:]:
        if line[0].isdigit():
            new_map.append([int(n) for n in line.split()])
        else:
            maps.append(new_map)
            new_map = []
    return maps + [new_map]


main()
