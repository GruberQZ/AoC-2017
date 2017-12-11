import os

input = open(os.getcwd() + '/Day9/input.txt')

withinGarbage = False

data = input.readline().rstrip()

# notGarbage = ''

skipNext = False

nestedLevel = 0

score = 0

canceled = 0

for char in data:
    if skipNext == True:
        skipNext = False
        continue
    if withinGarbage:
        if char == '>':
            # End of garbage
            withinGarbage = False
        elif char == '!':
            # Skip next character
            skipNext = True
        else:
            canceled += 1
    else:
        if char == '{':
            nestedLevel += 1
            score += nestedLevel
        elif char == '}':
            nestedLevel -= 1
        elif char == '<':
            withinGarbage = True

print(str(score))
print(str(canceled))
