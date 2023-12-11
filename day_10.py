with open("puzzle_inputs/day_10_input.txt") as file:
    lines = [list(line.rstrip("\n")) for line in file.readlines()]


class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.endings = self.get_endings()

    def get_endings(self):
        if lines[self.y][self.x] == "|":
            return (self.x, self.y-1), (self.x, self.y+1)
        if lines[self.y][self.x] == "-":
            return (self.x-1, self.y), (self.x+1, self.y)
        if lines[self.y][self.x] == "L":
            return (self.x, self.y-1), (self.x+1, self.y)
        if lines[self.y][self.x] == "J":
            return (self.x, self.y-1), (self.x-1, self.y)
        if lines[self.y][self.x] == "7":
            return (self.x-1, self.y), (self.x, self.y+1)
        if lines[self.y][self.x] == "F":
            return (self.x+1, self.y), (self.x, self.y+1)


def main():
  #  lines_cp = [["."]*len(lines[0])]*len(lines)
    start = get_start_pipe()
    convert_to_pipe_objects()
    previous = start
    current = (start[0], start[1]+1)
    length = 1
    while current != start:

        pipe_endings = lines[current[1]][current[0]].endings
        previous_cp = previous
        previous = current
        if pipe_endings[0] == previous_cp:
            current = pipe_endings[1]
        else:
            current = pipe_endings[0]
        length += 1
    print(length//2)




def convert_to_pipe_objects():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ".":
                lines[i][j] = Pipe(j, i)


def get_start_pipe():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return j, i





main()
