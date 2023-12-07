with open("puzzle_inputs/day_6_input.txt") as file:
    lines = file.readlines()

times = [time for time in lines[0].split(":")[1].split()]
distances = [dist for dist in lines[1].split(":")[1].split()]


def part_1():
    times_ints = [int(time) for time in times]
    distances_ints = [int(dist) for dist in distances]
    results = []
    for i in range(len(times_ints)):
        possibilities = 0
        for time in range(1, times_ints[i]):
            dist = get_distance(time, times_ints[i])
            if dist > distances_ints[i]:
                possibilities += 1
        results.append(possibilities)
    print(multiply_list(results))


def part_2():
    time = int("".join(times))
    distance = int("".join(distances))
    possibilities = 0
    for t in range(1, time):
        if get_distance(t, time) > distance:
            possibilities += 1
    print(possibilities)


def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def get_distance(charging_time, total_time):
    return (total_time - charging_time) * charging_time


part_1()
part_2()
