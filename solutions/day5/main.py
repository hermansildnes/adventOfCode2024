import math


def main():
    with open("input", "r") as file:
        sections = file.read().split("\n\n")
        rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]
        manuals = [list(map(int, line.split(","))) for line in sections[1].splitlines()]

    ordered_manuals = []
    for page in manuals:
        valid = True
        for first, last in rules:
            if first in page and last in page:
                if page.index(first) > page.index(last):
                    valid = False
                    break
        if valid:
            ordered_manuals.append(page)

    unique = []
    for el in ordered_manuals:
        if el not in unique:
            unique.append(el)

    sum = 0
    for el in unique:
        sum += el[math.ceil(len(el) / 2) - 1]

    print(sum)


if __name__ == "__main__":
    main()
