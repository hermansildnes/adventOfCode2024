# Did this one a few days later. Not quite sure why I didn't do
# it the same day as the first part considering how little extra
# effort it was... Anyways, my solution just flips the logic from part 1
# and then uses the same orderManual function to order the pages according
# to the given rules.

import math


def orderManual(page, rules):
    for el in page:
        for first, last in rules:
            if first in page and last in page:
                if page.index(first) > page.index(last):
                    page[page.index(first)], page[page.index(last)] = (
                        page[page.index(last)],
                        page[page.index(first)],
                    )
    return page


def main():
    with open("input", "r") as file:
        sections = file.read().split("\n\n")
        rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]
        manuals = [list(map(int, line.split(","))) for line in sections[1].splitlines()]

    unordered_manuals = set()
    for page in manuals:
        valid = True
        for first, last in rules:
            if first in page and last in page:
                if page.index(first) > page.index(last):
                    valid = False
                    break
        if not valid:
            unordered_manuals.add(tuple(page))

    sum = 0
    ordered_unordered = []
    for el in unordered_manuals:
        ordered_unordered.append(orderManual(list(el), rules))

    for el in ordered_unordered:
        sum += el[math.ceil(len(el) / 2) - 1]

    print(sum)


if __name__ == "__main__":
    main()
