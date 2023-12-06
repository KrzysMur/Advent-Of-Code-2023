with open("puzzle_inputs/day_6_input.txt") as file:
    lines = file.readlines()



def part_1():
    times = [int(time) for time in lines[0].split(":")[1].split()]
    distances = [int(dist) for dist in lines[1].split(":")[1].split()]
    results = []
    for i in range(len(times)):
        possibilities = 0
        for time in range(1, times[i]):
            dist = get_distance(time, times[i])
            if dist > distances[i]:
                possibilities += 1
        results.append(possibilities)
    print(multiply_list(results))


def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def get_distance(charging_time, total_time):
    return (total_time - charging_time) * charging_time


part_1()
