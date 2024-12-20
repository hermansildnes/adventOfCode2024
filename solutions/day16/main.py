# Yet again a puzzle that can be solved with BFS. Ripped getCurrentPos
# from day6/main.py and BFS from day10/main.py. The main difference is
# the implementations of a cost function to accomodate the different
# cost between moving straight and turning.

from collections import deque


def getCurrentPos(data, str):
    for i in range(len(data)):
        if str in data[i]:
            return (i, data[i].index(str))


def pathfind(maze, start, end):
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = set()
    queue = deque([(0, start[0], start[1], (0, 1))])

    while queue:
        min_cost_path = min(queue)
        queue.remove(min_cost_path)
        cost, current_row, current_col, prev_dir = min_cost_path

        if (current_row, current_col) == end:
            return cost

        if (current_row, current_col, prev_dir) in visited:
            continue

        visited.add((current_row, current_col, prev_dir))

        for move_row, move_col in directions:
            new_row = current_row + move_row
            new_col = current_col + move_col

            if maze[new_row][new_col] != "#":

                new_dir = (move_row, move_col)
                turn_cost = 1000 if prev_dir != new_dir else 0

                queue.append((cost + 1 + turn_cost, new_row, new_col, new_dir))
    return None


def main():
    with open("input", "r") as file:
        maze = [list(line.strip()) for line in file]

    start = getCurrentPos(maze, "S")
    end = getCurrentPos(maze, "E")
    sum = pathfind(maze, start, end)
    print(sum)


if __name__ == "__main__":
    main()
