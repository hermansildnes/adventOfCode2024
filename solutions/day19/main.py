# Okay so this took a while... Had code working on the example input
# but today the actual input took the challenge up multiple notches.
# For the actual input I ended up reworking the entire code. I realized
# after trying my initial naive approach for a while that I could reuse
# BFS from day10/main.py. Implementation is obviously slightly different
# but I ripped a lot (most) of the logic from day10/main.py.

from collections import deque


def main():
    with open("input", "r") as file:
        lines = file.read().strip().split("\n")
        available_strings = lines[0].split(", ")
        patterns = [pattern for pattern in lines[1:] if pattern]

    sum = 0

    for pattern in patterns:
        possible = False
        visited = set()
        queue = deque([0])

        while queue and not possible:
            pos = queue.popleft()
            if pos == len(pattern):
                possible = True
                break

            if pos in visited:
                continue
            visited.add(pos)

            for i in range(pos + 1, len(pattern) + 1):
                substring = pattern[pos:i]
                if substring in available_strings:
                    queue.append(i)

        sum += 1 if possible else 0

    print(sum)


if __name__ == "__main__":
    main()
