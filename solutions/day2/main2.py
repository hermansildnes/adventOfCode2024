def main():
    with open("input", "r") as file:
        data = [[int(num) for num in line.strip().split()] for line in file]

    sum = 0

    for report in data:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]
            increasing = all(
                1 <= modified_report[j + 1] - modified_report[j] <= 3
                for j in range(len(modified_report) - 1)
            )
            decreasing = all(
                1 <= modified_report[j] - modified_report[j + 1] <= 3
                for j in range(len(modified_report) - 1)
            )
            if increasing or decreasing:
                sum += 1
                break
    print(sum)


if __name__ == "__main__":
    main()
