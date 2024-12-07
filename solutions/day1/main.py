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

    arr1.sort()
    arr2.sort()

    sum = 0

    for i in range(len(arr1)):
        sum += abs(arr1[i] - arr2[i])

    print(sum)


if __name__ == "__main__":
    main()
