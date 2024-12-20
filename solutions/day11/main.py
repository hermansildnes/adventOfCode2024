# Part 1 wasreally simple. Reminds me of some cellular automata
# I've done some work with in the past. Love the simplicity of
# part 2, but the nature of the challenge makes it impossible
# to solve without actually running through all the iterations,
# and no matter my optimizations (including doing it in C++),
# I still run out of resources or it takes too long... I got
# rid of the string/int casting in my attempts at part 2, but
# kept them here cause it was my original (although awful)
# approach


def main():
    with open("input", "r") as file:
        lines = file.readlines()
        data = [el for line in lines for el in line.split(" ")]

    new = []
    for i in range(25):
        for el in data:
            if len(el) % 2 == 0:
                new.append(str(int(el[: len(el) // 2])))
                new.append(str(int(el[len(el) // 2 :])))
            elif el == "0":
                new.append("1")
            else:
                new.append(str(int(el) * 2024))
        data = new
        new = []

    print(len(data))


if __name__ == "__main__":
    main()
