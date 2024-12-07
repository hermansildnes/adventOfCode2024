# Adding extra regex to the code in day3/main.py to find
# all do(), don't() in addition to  mul(x, y) instructions.
# Then, all the instructions are iterated over and each time
# a do() or don't() is found, the mul flag is toggled.

import re


def mul(x, y):
    return x * y


def main():
    with open("input", "r") as file:
        content = file.read()

    mul_pattern = r"mul\((\d+),(\d+)\)"
    do = r"do\(\)"
    dont = r"don't\(\)"

    mul_flag = True
    sum = 0

    instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", content)

    for instruction in instructions:
        if re.match(do, instruction):
            mul_flag = True
        elif re.match(dont, instruction):
            mul_flag = False
        elif re.match(mul_pattern, instruction):
            if mul_flag:
                sum += eval(instruction)

    print(sum)


if __name__ == "__main__":
    main()
