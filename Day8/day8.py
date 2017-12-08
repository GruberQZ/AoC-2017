import os
import re

input = open(os.getcwd() + '\Day8\input.txt')

instRegex = re.compile(r'(\w+)\s(\w+)\s(-*\d+)\sif\s(\w+)\s([<>=!]+)\s(-*\d+)')

regs = {}

highestRegValueEver = 0

for line in input:
    match = instRegex.match(line.rstrip().replace('\n', ''))
    destReg = match.group(1)
    operand = match.group(2)
    amount = int(match.group(3))
    srcReg = match.group(4)
    comparator = match.group(5)
    value = int(match.group(6))
    # Check to see if both src and dest exist
    if destReg not in regs:
        regs[destReg] = 0
    if srcReg not in regs:
        regs[srcReg] = 0
    # Use comparator to figure out if instruction should be taken
    doInstruction = False
    if comparator == '>':
        if regs[srcReg] > value:
            doInstruction = True
    elif comparator == '<':
        if regs[srcReg] < value:
            doInstruction = True
    elif comparator == '<=':
        if regs[srcReg] <= value:
            doInstruction = True
    elif comparator == '>=':
        if regs[srcReg] >= value:
            doInstruction = True
    elif comparator == '==':
        if regs[srcReg] == value:
            doInstruction = True
    elif comparator == '!=':
        if regs[srcReg] != value:
            doInstruction = True
    if doInstruction:
        if operand == 'inc':
            regs[destReg] += amount
        else:
            regs[destReg] -= amount
    # Check for highest value ever in a register
    if regs[destReg] > highestRegValueEver:
        highestRegValueEver = regs[destReg]

maxValue = -1000000
maxReg = ''
for regName, regValue in regs.items():
    if regValue > maxValue:
        maxValue = regValue
        maxReg = regName

print(str(maxValue))
print(str(highestRegValueEver))