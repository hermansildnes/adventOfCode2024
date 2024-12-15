def getCurrentPos(data):
    for i in range(len(data)):
        if "^" in data[i]:
            return (i, data[i].index("^"))


def getNewPos(current_pos, current_direction):
    return (
        current_pos[0] + current_direction[0],
        current_pos[1] + current_direction[1],
    )

def checkLoop(data, current_pos):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = directions[3]
    visited = set()
    visited.add((current_pos, current_direction))
    while True:
        try:
            new_pos = getNewPos(current_pos, current_direction)
            if (new_pos, current_direction) in visited:
                return True
            assert (
                new_pos[0] >= 0
                and new_pos[1] >= 0
                and new_pos[0] < len(data)
                and new_pos[1] < len(data[0])
            )
            if data[new_pos[0]][new_pos[1]] == "#":
                current_direction = directions[
                    (directions.index(current_direction) + 1) % 4
                ]
                new_pos = getNewPos(current_pos, current_direction)
            visited.add((new_pos, current_direction))
            current_pos = new_pos
        except AssertionError:
            return False
    return False


def main():
    with open("input2", "r") as f:
        data = [[char for char in word] for line in f for word in line.strip().split()]

    sum = 0
    copy = data.copy()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if copy[i][j] != "^" and copy[i][j] != "#":
                copy[i][j] = "#"
            print("Checking if ", (i, j), " causes a loop")
            if checkLoop(copy, getCurrentPos(copy)):
                sum += 1
            

    print(sum)


if __name__ == "__main__":
    main()
