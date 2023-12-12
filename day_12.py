import itertools

with open("puzzle_inputs/day_12_input.txt") as file:
    lines = [[line[0], [int(num) for num in line[1].split(",")]]
             for line in [l.strip().split()
                          for l in file.readlines()]]


def main():
    total = 0
    for line in lines:
        total += count_possible_layouts(line)
    print(total)


def count_possible_layouts(line: list[str, list[int]]):
    sequence, block_counts = line
    hashes_to_insert = sum(block_counts) - sequence.count("#")
    combinations = list(itertools.combinations(list(range(sequence.count("?"))), hashes_to_insert))
    counter = 0

    for combination in combinations:
        current_combination = get_combination(combination, sequence)
        if is_layout_valid(current_combination, block_counts):
            counter += 1

    return counter


def get_combination(combination, sequence):
    question_mark_indexes = get_question_mark_indexes(sequence)
    for i in range(len(question_mark_indexes)):
        if i in combination:
            sequence = replace_with_hash(sequence, question_mark_indexes[i])
        else:
            sequence = replace_with_dot(sequence, question_mark_indexes[i])
    return sequence


def get_question_mark_indexes(sequence):
    return [i for i in range(len(sequence)) if sequence[i] == "?"]


def is_layout_valid(sequence: str, block_counts: list[int]):
    blocks = [block for block in sequence.split(".") if block]
    if len(blocks) == len(block_counts):
        for i in range(len(blocks)):
            if len(blocks[i]) != block_counts[i]:
                return False
        return True
    return False


def replace_with_hash(sequence: str, index: int):
    return sequence[:index] + "#" + sequence[index + 1:]


def replace_with_dot(sequence: str, index: int):
    return sequence[:index] + "." + sequence[index + 1:]


main()
