# Quite similar to day6, so ripped some code from day6/main.py
# Main difference is the way the grid is updated, which I do recursively
# here to accomodate boxes pushing boxes. Otherwise, quite straight
# forward. Just a matter of reading the instructions and updating the grid.
# Ran into some trouble because I did not make a deep copy of the
# grid at first...


def getCurrentPos(data, str):
    for i in range(len(data)):
        if str in data[i]:
            return (i, data[i].index(str))


def updateGrid(grid, current_pos, current_instruction):
    newGrid = [row[:] for row in grid]
    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    nextPos = (
        current_pos[0] + directions[current_instruction][0],
        current_pos[1] + directions[current_instruction][1],
    )
    if grid[nextPos[0]][nextPos[1]] == "#":
        return newGrid
    if grid[nextPos[0]][nextPos[1]] == ".":
        newGrid[nextPos[0]][nextPos[1]], newGrid[current_pos[0]][current_pos[1]] = (
            newGrid[current_pos[0]][current_pos[1]],
            newGrid[nextPos[0]][nextPos[1]],
        )

        return newGrid

    if newGrid[nextPos[0]][nextPos[1]] == "O":
        pushResult = updateGrid(newGrid, nextPos, current_instruction)
        if pushResult != grid:
            (
                pushResult[nextPos[0]][nextPos[1]],
                pushResult[current_pos[0]][current_pos[1]],
            ) = (
                pushResult[current_pos[0]][current_pos[1]],
                pushResult[nextPos[0]][nextPos[1]],
            )
            return pushResult

    return newGrid


def main():
    with open("input", "r") as file:
        data = file.read().split("\n\n")
        grid = [list(line) for line in data[0].splitlines()]
        instructions = [char for char in data[1] if char != "\n"]

    for instruction in instructions:
        current_pos = getCurrentPos(grid, "@")
        grid = updateGrid(grid, current_pos, instruction)

    sum = 0
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "O":
                sum += (i * 100) + j

    print(sum)


if __name__ == "__main__":
    main()
