import os

input = open(os.getcwd() + '/Day10/input.txt')

inputLengths = []

lengths = input.readline().split(',')
for length in lengths:
    inputLengths.append(int(length))

circularList = []
for i in range(256):
    circularList.append(i)

currentPosition = 0

skipSize = 0

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

# Multiply values in 0 and 1 indecies of circularList
print(str(circularList[0] * circularList[1]))