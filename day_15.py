with open("puzzle_inputs/day_15_input.txt") as file:
    instructions = file.read().split(",")


def main():
    total_sum = 0
    for instruction in instructions:
        total_sum += hash_algorithm(instruction)
    print(total_sum)

def hash_algorithm(text):
    current_value = 0
    for char in text:
        current_value = (17 * (current_value + ord(char))) % 256
    return current_value


main()
