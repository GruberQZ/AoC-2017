import os

input = open(os.getcwd() + '/Day10/input.txt').readline()

# input = '1,2,3'

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

denseHash = []
for i in range(int(256/16)):
    currentList = circularList[i*16:(i+1)*16]
    result = currentList[0]
    for j in range(1, len(currentList)):
        result ^= currentList[j]
    denseHash.append(result)

final = ''
for entry in denseHash:
    hexVal = hex(entry)[2:]
    if len(hexVal) == 1:
        final += '0' + hexVal
    else:
        final += hexVal

print(final)