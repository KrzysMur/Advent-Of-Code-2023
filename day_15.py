with open("puzzle_inputs/day_15_input.txt") as file:
    instructions = file.read().split(",")

parsed_instructions = [[pair[0], int(pair[1])] if len(pair) == 2 else [pair[0][:-1]]
                       for pair in [instruction.split("=")
                                    for instruction in instructions]]


def part_1():
    total_sum = 0

    for instruction in instructions:
        total_sum += hash_algorithm(instruction)

    print(total_sum)


def part_2():
    boxes = {i: {} for i in range(256)}

    for instruction in parsed_instructions:
        box_index = hash_algorithm(instruction[0])

        if len(instruction) == 2:
            boxes[box_index].update({instruction[0]: instruction[1]})

        else:
            boxes[box_index].pop(instruction[0], None)

    focusing_power = count_focusing_power(boxes)
    print(focusing_power)


def count_focusing_power(boxes: dict):
    total = 0

    for i in range(len(boxes)):
        items = list(boxes[i].items())
        for j in range(len(items)):
            total += items[j][1] * (j+1) * (i+1)

    return total



def hash_algorithm(text: str):
    current_value = 0
    for char in text:
        current_value = (17 * (current_value + ord(char))) % 256

    return current_value


part_1()
part_2()
