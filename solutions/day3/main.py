import re


def mul(x, y):
    return x * y


def main():
    with open("input", "r") as file:
        content = file.read()

    matches = re.findall(r"mul\(\d+,\d+\)", content)
    sum = 0

    for instruction in matches:
        sum += eval(instruction)

    print(sum)


if __name__ == "__main__":
    main()
