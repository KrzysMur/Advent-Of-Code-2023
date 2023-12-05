with open("puzzle_inputs/day_4_input.txt") as file:
    lines = [line.rstrip("\n").split(":")[1]for line in file.readlines()]


def count_duplicates(list1, list2):
    duplicates = 0
    for n in list1:
        if n in list2:
            duplicates += 1
    return duplicates


def part_1():
    total_sum = 0
    for line in lines:
        winning_numbers, scratchcard_numbers = [[int(n) for n in numbers.split()] for numbers in line.split("|")]
        number_of_winning_numbers = count_duplicates(winning_numbers, scratchcard_numbers)
        total_sum += int(2 ** (number_of_winning_numbers-1))

    print(total_sum)


def part_2():
    copies = {v: 1 for v in range(len(lines))}
    for i in range(len(lines)):
        winning_numbers, scratchcard_numbers = [[int(n) for n in numbers.split()] for numbers in lines[i].split("|")]
        duplicates = count_duplicates(winning_numbers, scratchcard_numbers)
        for j in range(1, duplicates+1):
            copies[i+j] += copies[i]

    print(sum([v for v in copies.values()]))


part_1()
part_2()
