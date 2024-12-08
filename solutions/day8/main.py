# Took way longer than it should have, but got it working in the end.
# Kept getting almost all the antinodes, but not all of them and couldn't
# figure out why just a couple were missing. Got it in the end by redoing
# calculateAntinodes() and rethinking the logic. Don't love the fundamental
# approach - a bit too nested - but it seems to be efficient enough.


def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


def calculateAntinodes(index1, index2):
    dist_x, dist_y = index2[0] - index1[0], index2[1] - index1[1]
    antiNode1, antiNode2 = (index1[0] - dist_x, index1[1] - dist_y), (
        index2[0] + dist_x,
        index2[1] + dist_y,
    )

    result = []
    for antinode in (antiNode1, antiNode2):
        dist1 = distance(antinode, index1)
        dist2 = distance(antinode, index2)
        if abs(dist1 * 2 - dist2) < 0.0001 or abs(dist2 * 2 - dist1) < 0.0001:
            result.append(antinode)

    return tuple(result)


def is_within_bounds(point, grid):
    x, y = point
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
                            antinodes = calculateAntinodes((i, j), (k, l))
                            for antinode in antinodes:
                                if is_within_bounds(antinode, grid):
                                    nodes.add(antinode)

    for element in nodes:
        print(element)
    print(len(nodes))


if __name__ == "__main__":
    main()
