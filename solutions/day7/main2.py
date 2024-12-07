# The logic is the same as day7/main.py, but with an extra operator.
# The extra operator "|" significantly reduces the performance, due to
# the number of operator combinations that must be checked. A more optimal
# solution is surely achievable, but with a runtime of ~10s it is acceptable
# for now.

import itertools


def getOperators(row, result):
    operators = list(itertools.product("*+|", repeat=len(row) - 1))
    for operator in operators:
        current = row[0]
        for i in range(len(operator)):
            if operator[i] == "+":
                current += row[i + 1]
            elif operator[i] == "*":
                current *= row[i + 1]
            else:
                current = int(str(current) + str(row[i + 1]))
        if current == result:
            return True
    return False


def main():
    with open("input", "r") as file:
        data = []
        for line in file:
            row = list(map(lambda x: int(x.replace(":", "")), line.split()))
            data.append(row)

    sum = 0
    for row in data:
        result = row[0]
        factors = row[1:]
        if getOperators(factors, result):
            sum += result

    print(sum)


if __name__ == "__main__":
    main()
