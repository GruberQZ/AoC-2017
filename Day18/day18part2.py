
import os
import os.path
import copy

# Things to keep:
# - Program Counter
# - Regs for each instance
# - Receive queue for each instance

# Things that remain the same:
# - Instructions

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def duet(instructions, programCounter, regs, receiveQueue):
    instructions = instructions
    pc = programCounter
    regs = regs
    receiveQueue = receiveQueue
    sendQueue = []
    instsExecuted = 0

    # Process instructions
    lenInstructions = len(instructions)
    lastSound = 0
    while pc >= 0 and pc < lenInstructions:
        curInst = instructions[pc]
        if curInst[0] == 'snd':
            # Play a sound with freq X
            x = curInst[1]
            if representsInt(x):
                sendQueue.append(int(x))
            else:
                sendQueue.append(regs[x])
        elif curInst[0] == 'set':
            # Set reg value from int or other reg
            x = curInst[1]
            y = curInst[2]
            if representsInt(y):
                regs[x] = int(y)
            else:
                regs[x] = regs[y]
        elif curInst[0] == 'add':
            # Set reg value from int or other reg
            x = curInst[1]
            y = curInst[2]
            if representsInt(y):
                regs[x] += int(y)
            else:
                regs[x] += regs[y]
        elif curInst[0] == 'mul':
            # Set reg value from int or other reg
            x = curInst[1]
            y = curInst[2]
            if representsInt(y):
                regs[x] *= int(y)
            else:
                regs[x] *= regs[y]
        elif curInst[0] == 'mod':
            # Set reg value from int or other reg
            x = curInst[1]
            y = curInst[2]
            if representsInt(y):
                regs[x] %= int(y)
            else:
                regs[x] %= regs[y]
        elif curInst[0] == 'rcv':
            # # Recover freq of last sound played
            # if representsInt(x):
            #     valX = int(x)
            # else:
            #     valX = regs[x]
            # if valX > 0:
            #     return lastSound
            # Pull a value from the receiveQueue
            x = curInst[1]
            if len(receiveQueue) > 0:
                regs[x] = receiveQueue.pop(0)
            else:
                return instsExecuted, pc, regs, sendQueue 
        elif curInst[0] == 'jgz':
            # Jump
            x = curInst[1]
            y = curInst[2]
            if representsInt(x):
                valX = int(x)
            else:
                valX = regs[x]
            if valX > 0:
                if representsInt(y):
                    pc += int(y)
                else:
                    pc += regs[y]
                instsExecuted += 1
                continue
        # Increment the program counter
        instsExecuted += 1
        pc += 1

# Get instructions
input = open(os.path.join(os.getcwd(), 'Day18', 'input.txt'))
instructions = []
for line in input:
    instructions.append(line.rstrip().split())

# Figure out all the possible registers
regs = {}
for inst in instructions:
    for operand in inst[1:]:
        if not representsInt(operand):
            regs[operand] = 0

# Program counters for each program
prog0pc = 0
prog1pc = 0

# Make a copy of registers for each program
prog0Regs = copy.copy(regs)
prog1Regs = copy.copy(regs)
prog1Regs['p'] = 1

# Receive queue for each program
prog0ReceiveQueue = []
prog1ReceiveQueue = []

prog1TimesSentValue = 0
prog0InstsExecuted = 1
prog1InstsExecuted = 1
count = 0
while prog0InstsExecuted > 0 or prog1InstsExecuted > 0:
    # Run each program
    # Program 0
    prog0InstsExecuted, prog0pc, prog0Regs, prog1ReceiveQueue = \
        duet(instructions, prog0pc, prog0Regs, prog0ReceiveQueue)
    # Program 1
    prog1InstsExecuted, prog1pc, prog1Regs, prog0ReceiveQueue = \
        duet(instructions, prog1pc, prog1Regs, prog1ReceiveQueue)
    # Count
    # Length of prog0's receive queue is the number of times
    # prog1 sent a value
    count += len(prog0ReceiveQueue)

print(str(count))