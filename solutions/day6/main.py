def getCurrentPos(data):
    for i in range(len(data)):
        if "^" in data[i]:
            return (i, data[i].index("^"))


def getNewPos(current_pos, current_direction):
    return (
        current_pos[0] + current_direction[0],
        current_pos[1] + current_direction[1],
    )


def main():
    with open("input", "r") as f:
        data = [[char for char in word] for line in f for word in line.strip().split()]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    current_direction = directions[3]
    current_pos = getCurrentPos(data)
    visited = set()
    visited.add(current_pos)
    while True:
        try:
            new_pos = getNewPos(current_pos, current_direction)
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
            visited.add(new_pos)
            current_pos = new_pos
        except AssertionError:
            break

    print(len(visited))


if __name__ == "__main__":
    main()
