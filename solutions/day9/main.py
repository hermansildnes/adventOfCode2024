# Part 1 was pretty easy today

def unpackData(data):
    unpacked = []
    index = 0
    for i, char in enumerate(data):
        if i % 2 == 0:
            for _ in range(int(char)):
                unpacked.append(index)
            index += 1
        else:
            for _ in range(int(char)):
                unpacked.append(" ")
    return unpacked

def calcChecksum(data):
    sum = 0
    for i, value in (enumerate(data)):
        sum += i * value
    return sum

def main():
    with open("input", "r") as file:
        data = file.read()    

    unpacked = unpackData(data)

    for i, value in enumerate(unpacked):
        while unpacked[-1] == " ":
            unpacked.pop()
        if value == " ":
            unpacked[i], unpacked[-1] = unpacked[-1], unpacked[i]

    print(calcChecksum(unpacked))


if __name__ == "__main__":
    main()