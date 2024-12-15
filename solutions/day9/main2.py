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

def getBlocks(data):
    blocks = []
    block = []
    for el in data:
        if el == " ":
            if block and block[-1] != " ":
                blocks.append(block)
                block = []
            block.append(el)
        else:
            if block and block[-1] != el:
                blocks.append(block)
                block = []
            block.append(el)
    if block:
        blocks.append(block)
    return blocks

def calcChecksum(data):
    sum = 0
    for i, value in (enumerate(data)):
        sum += i * int(value)
    return sum

def main():
    with open("input2", "r") as file:
        data = file.read()    

    unpacked = unpackData(data)

    # for el in unpacked:
    #     print(el, end="")

    blocks = getBlocks(unpacked)
    # print(blocks)
    #print(calcChecksum(unpacked))


    for i, block in enumerate(blocks[::-1]):
        while blocks[-1][0] == " ":
            blocks.pop()
        for j, _block in enumerate(blocks):
            if _block[0] == " ":
                if len(_block) <= len(block):
                    blocks[j], blocks[i] = blocks[i], blocks[j]
                    break

    for block in sorted:
        print(block)
                

if __name__ == "__main__":
    main()