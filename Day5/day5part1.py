import os

input = open(os.getcwd() + '\Day5\input.txt')

insts = []

for line in input:
    insts.append(int(line.rstrip()))

currentInst = 0
steps = 0
newInst = 0

while newInst >= 0 and newInst < len(insts):
    currentInst = newInst
    newInst = currentInst + insts[currentInst]
    insts[currentInst] += 1
    steps += 1
    

print(str(steps))