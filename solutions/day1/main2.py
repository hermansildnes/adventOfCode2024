def main():
    columns = []
    with open("input", "r") as file:
        for line in file:
            numbers = list(map(int, line.split()))
            if not columns:
                columns = [[] for _ in range(len(numbers))]
            for i, number in enumerate(numbers):
                columns[i].append(number)

    arr1 = columns[0]
    arr2 = columns[1]

    sum = 0

    for number in arr1:
        temp = 0
        for number2 in arr2:
            if number2 == number:
                temp += 1
        sum += number * temp

    print(sum)


if __name__ == "__main__":
    main()
