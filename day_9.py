with open("puzzle_inputs/day_9_input.txt") as file:
    lines = [[int(num) for num in line.split()] for line in file.readlines()]


def part_1():
    extrapolated_sum = 0
    for sequence in lines:
        extrapolated_sum += extrapolate(sequence)
    print(extrapolated_sum)


def part_2():
    extrapolated_sum = 0
    for sequence in lines:
        extrapolated_sum += extrapolate_backwords(sequence)
    print(extrapolated_sum)


def extrapolate(sequence):
    layers = get_layers(sequence)
    return sum([layer[-1] for layer in layers])


def extrapolate_backwords(sequence):
    layers = get_layers(sequence)
    for i in range(len(layers)-1, 0, -1):
        x = layers[i-1][0] - layers[i][0]
        layers[i-1].insert(0, x)
    return layers[0][0]


def get_layers(sequence):
    layers = [sequence]
    while not all_zeros(layers[-1]):
        new_layer = []
        for i in range(1, len(layers[-1])):
            new_layer.append(layers[-1][i] - layers[-1][i - 1])
        layers.append(new_layer)
    return layers


def all_zeros(sequence):
    for number in sequence:
        if number != 0:
            return False
    return True


part_1()
part_2()
