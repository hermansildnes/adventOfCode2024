# Not worked on again, but solution should be quite straight
# forward.


from collections import deque


def getRegions(grid):
    regions = set()
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            regions.add(BFS(grid, (i, j)))

    return regions


def BFS(grid, start):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    queue = deque([start])
    while queue:
        plant = queue.popleft()
        if plant not in visited:
            visited.add(plant)
            for direction in directions:
                if (
                    0 <= plant[0] + direction[0] < len(grid)
                    and 0 <= plant[1] + direction[1] < len(grid[0])
                ) and grid[plant[0] + direction[0]][plant[1] + direction[1]] == grid[
                    start[0]
                ][
                    start[1]
                ]:
                    new_plant = (plant[0] + direction[0], plant[1] + direction[1])
                    if new_plant not in visited:
                        queue.append(new_plant)
    return frozenset(visited)


def calculateRegionPrice(region):
    perimeter = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for plant_x, plant_y in region:
        for direction in directions:
            if (plant_x + direction[0], plant_y + direction[1]) not in region:
                perimeter += 1
    return perimeter * len(region)


def main():
    with open("input", "r") as file:
        grid = [[char for char in line.strip()] for line in file.readlines()]

    sum = 0
    for region in getRegions(grid):
        sum += calculateRegionPrice(region)

    print(sum)


if __name__ == "__main__":
    main()
