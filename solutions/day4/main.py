def checkDirection(grid, start_x, start_y, delta_x, delta_y):
    for i in range(4):
        current_x = start_x + i * delta_x
        current_y = start_y + i * delta_y

        if not (0 <= current_x < len(grid) and 0 <= current_y < len(grid[0])):
            return False

        if grid[current_x][current_y] != "XMAS"[i]:
            return False

    return True


def main():
    with open("input", "r") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]

    directions = [
        (1, 0),  # Right
        (-1, 0),  # Left
        (0, -1),  # Up
        (0, 1),  # Down
        (1, 1),  # Down-right
        (1, -1),  # Down-left
        (-1, 1),  # Up-right
        (-1, -1),  # Up-left
    ]

    sum = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for delta_x, delta_y in directions:
                if checkDirection(grid, row, col, delta_x, delta_y):
                    sum += 1

    print(sum)


if __name__ == "__main__":
    main()
