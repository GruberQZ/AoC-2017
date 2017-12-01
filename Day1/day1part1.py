
file = open('d:\AoC-2017\Day1\input.txt', 'r')

input = file.readline().rstrip()

total = 0

for charIndex in range(len(input)):
    currentChar = input[charIndex]
    if charIndex == len(input) - 1:
        if currentChar == input[0]:
            total += int(currentChar)
    elif currentChar == input[charIndex+1]:
        total += int(currentChar)

print(str(total))
