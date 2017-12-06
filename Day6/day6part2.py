import os

input = open(os.getcwd() + '\Day6\input.txt')

banks = input.readline().rstrip().split()

for x in range(len(banks)):
    banks[x] = int(banks[x])

uniqueSets = set()

uniqueSetsDict = {}

count = 0
while True:
    # Find largest in list
    maxValue = max(banks)
    # Find lowest index of maxValue in banks
    index = banks.index(maxValue)
    # Clear value of bank
    banks[index] = 0
    # Add circularly until out
    while maxValue:
        # Figure out next index
        if index == len(banks) - 1:
            index = 0
        else:
            index += 1
        # Add 1 to position
        banks[index] += 1
        # Dec maxValue
        maxValue -= 1
    count += 1
    # Make tuple out of banks arrangement, add to set
    banksTuple = tuple(banks)
    if banksTuple in uniqueSetsDict:
        break
    else:
        uniqueSetsDict[banksTuple] = count

print(str(count - uniqueSetsDict[tuple(banks)]))