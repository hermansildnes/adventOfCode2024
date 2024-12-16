# After a couple more challenging days, this one was quite
# a bit easier. No need to even populate an array, just
# update the positions according to the defined velocites.
# Then, simply do the counting and finito. Noticed that the
# file parsing has gotten a bit more challenging in the last
# few days too, but that is just good practice.


def main():
    with open("input", "r") as file:
        data = []
        for line in file:
            parts = line.strip().split()
            pos = tuple(map(int, parts[0][2:].split(",")))
            vel = tuple(map(int, parts[1][2:].split(",")))
            data.append((pos, vel))

    width = 101
    height = 103
    for i in range(100):
        for j in range(len(data)):
            new_x = (data[j][0][0] + data[j][1][0]) % width
            new_y = (data[j][0][1] + data[j][1][1]) % height
            data[j] = ((new_x, new_y), data[j][1])

    quadrants = [0, 0, 0, 0]
    for pos, vel in data:
        x, y = pos
        if x == width // 2 or y == height // 2:
            continue
        if x < width // 2 and y < height // 2:
            quadrants[0] += 1
        elif x >= width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x < width // 2 and y >= height // 2:
            quadrants[2] += 1
        else:
            quadrants[3] += 1

    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


if __name__ == "__main__":
    main()
