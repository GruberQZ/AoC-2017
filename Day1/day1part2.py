
file = open('d:\AoC-2017\Day1\input.txt', 'r')

input = file.readline().rstrip()

total = 0

charsToSkip = int(len(input)/2)

for charIndex in range(len(input)):
    currentChar = input[charIndex]
    if charIndex + charsToSkip > len(input) - 1:
        compChar = input[charIndex - charsToSkip]
    else:
        compChar = input[charIndex + charsToSkip]
    if currentChar == compChar:
        total += int(currentChar)

print(str(total))
