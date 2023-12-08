
def read_data():
    with open("puzzle_inputs/day_8_input.txt") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]
    instructions = ["0" if instruction == "L" else "1" for instruction in lines.pop(0)]

    nodes = {}
    for line in lines[1:]:
        key, value = line.split(" = ")
        value = [v.strip("()") for v in value.split(", ")]
        nodes.update({key: value})
    return instructions, nodes


def part_1():
    instructions, nodes = read_data()
    next_key = "AAA"
    counter = 0
    while next_key != "ZZZ":
        next_key = nodes[next_key][int(instructions[counter % len(instructions)])]
        counter += 1
    print(counter)





part_1()
