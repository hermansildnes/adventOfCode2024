# Redid the calculateAntinodes() function to use a slope approach
# that finds each point on the line through two nodes that
# is an integer, and thus a valid index in the grid.


def calculateAntinodes(index1, index2, grid):
    antinodes = []
    x1, y1 = index1
    x2, y2 = index2

    extension = max(len(grid), len(grid[0]))

    if x2 - x1 == 0:
        min_y = -extension
        max_y = extension
        for y in range(min_y, max_y):
            antinodes.append((x1, y))
    else:
        slope = (y2 - y1) / (x2 - x1)
        min_x = -extension
        max_x = extension

        for x in range(min_x, max_x):
            y = slope * (x - x1) + y1
            if y.is_integer():
                antinodes.append((x, int(y)))

    return tuple(antinodes)


def is_within_bounds(index, grid):
    x, y = index
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def main():
    with open("input", "r") as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]

    nodes = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                for k in range(len(grid)):
                    for l in range(len(grid[k])):
                        if k == i and l == j:
                            continue
                        if grid[k][l] == grid[i][j]:
                            antinodes = calculateAntinodes((i, j), (k, l), grid)
                            for antinode in antinodes:
                                if is_within_bounds(antinode, grid):
                                    nodes.add(antinode)

    print(len(nodes))


if __name__ == "__main__":
    main()
