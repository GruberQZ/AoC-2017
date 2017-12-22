
import os
import os.path

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def duet():
    instructions = []
    pc = 0
    regs = {}

    # Get instructions
    input = open(os.path.join(os.getcwd(), 'Day18', 'input.txt'))
    for line in input:
        instructions.append(line.rstrip().split())

    # Figure out all the possible registers
    for inst in instructions:
        for operand in inst[1:]:
            if not representsInt(operand):
                regs[operand] = 0

    # Process instructions
    lenInstructions = len(instructions)
    lastSound = 0
    while pc >= 0 and pc < lenInstructions:
        curInst = instructions[pc]
        if curInst[0] == 'snd':
            # Play a sound with freq X
            x = curInst[1]
            lastSound = regs[x]
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
            # Recover freq of last sound played
            if representsInt(x):
                valX = int(x)
            else:
                valX = regs[x]
            if valX > 0:
                return lastSound
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
                continue
        # Increment the program counter
        pc += 1
                
print(str(duet()))