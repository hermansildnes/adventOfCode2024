def main():
    with open("input", "r") as file:
        data = [[int(num) for num in line.strip().split()] for line in file]

    sum = 0
    for report in data:
        increasing = all(
            1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)
        )
        decreasing = all(
            1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1)
        )
        if increasing or decreasing:
            sum += 1
    print(sum)


if __name__ == "__main__":
    main()
