
def knot_hash(input):
    circularList = []
    for i in range(256):
        circularList.append(i)

    inputLengths = []
    for char in input:
        inputLengths.append(ord(char))

    inputLengths.append(17)
    inputLengths.append(31)
    inputLengths.append(73)
    inputLengths.append(47)
    inputLengths.append(23)

    currentPosition = 0

    skipSize = 0

    for i in range(64):
        for inputLength in inputLengths:
            # Build a list from current position onward
            # that is inputLength + skipSize long
            currentList = []
            index = currentPosition
            while len(currentList) != inputLength:
                currentList.append(circularList[index])
                if index == len(circularList) - 1:
                    index = 0
                else:
                    index += 1
            # Reverse the list
            currentList.reverse()
            # Insert reversed elements back into list
            index = currentPosition
            for entry in currentList:
                circularList[index] = entry
                if index == len(circularList) - 1:
                    index = 0
                else:
                    index += 1
            # Move the current position up by inputLength + skipSize
            currentPosition += inputLength + skipSize
            while currentPosition >= len(circularList):
                currentPosition -= len(circularList)
            # Increment skipSize
            skipSize += 1

    final = ''
    for i in range(int(256/16)):
        currentList = circularList[i*16:(i+1)*16]
        result = currentList[0]
        for j in range(1, len(currentList)):
            result ^= currentList[j]
        final += bin(result).lstrip('-0b').zfill(8)

    # final = ''
    # for entry in denseHash:
    #     hexVal = hex(entry)[2:]
    #     if len(hexVal) == 1:
    #         final += '0' + hexVal
    #     else:
    #         final += hexVal

    return final

input = 'jxqlasbh'

count = 0
unexplored = set()
for i in range(128):
    hash = knot_hash(input + '-' + str(i))
    for j in range(len(hash)):
        if hash[j] == '1':
            count += 1
            unexplored.add((i, j))

print(str(count))

groups = 0
while len(unexplored) > 0:
    # Pop a random position out of unexplored
    neighbors = set()
    node = unexplored.pop()
    unexplored.add(node)
    neighbors.add(node)
    # See if any of this node's neighbors are unexplored
    while len(neighbors) > 0:
        node = neighbors.pop()
        unexplored.remove(node)
        possibleNeighbors = []
        if node[1] - 1 > -1:
            possibleNeighbors.append((node[0], node[1] - 1))
        if node[1] + 1 < 128:
            possibleNeighbors.append((node[0], node[1] + 1))
        if node[0] - 1 > -1:
            possibleNeighbors.append((node[0] - 1, node[1]))
        if node[0] + 1 < 128:
            possibleNeighbors.append((node[0] + 1, node[1]))
        for possibleNeighbor in possibleNeighbors:
            if possibleNeighbor in unexplored:
                neighbors.add(possibleNeighbor)
    # Inc groups
    groups += 1

print(str(groups))
