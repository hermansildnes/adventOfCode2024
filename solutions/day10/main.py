# Took me a bit too come up with a good solution for this one,
# but in the end I realized I could just do breadth first
# search... Did not want to do it recursively so that made it
# bit more tricky.

from collections import deque


def getIndex(grid, value):
    idx = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == value:
                idx.append((i, j))
    return idx


def BFS(grid, start_position):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = set()
    queue = deque([(start_position[0], start_position[1], 0)])
    nines = set()

    while queue:
        current_row, current_col, next_num = queue.popleft()

        if grid[current_row][current_col] == 9:
            nines.add((current_row, current_col))
            continue

        visited.add((current_row, current_col))

        for move_row, move_col in directions:
            new_row = current_row + move_row
            new_col = current_col + move_col

            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid)
                and (new_row, new_col) not in visited
            ):
                if grid[new_row][new_col] == next_num + 1:
                    queue.append((new_row, new_col, next_num + 1))

    return len(nines)


def main():
    with open("input", "r") as file:
        lines = file.readlines()
    grid = [[int(char) for char in line.strip()] for line in lines]

    trailheads = getIndex(grid, 0)

    sum = 0
    for start in trailheads:
        nines = BFS(grid, start)
        print(nines)
        sum += nines

    print(sum)


if __name__ == "__main__":
    main()
