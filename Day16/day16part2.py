
import os
import os.path
import re
import copy

spinRegex = re.compile(r's(\d+)')
exchangeRegex = re.compile(r'x(\d+)\/(\d+)')
partnerRegex = re.compile(r'p(\w+)\/(\w+)')

input =  open(os.path.join(os.getcwd(), 'Day16', 'input.txt'), 'r')
moves = input.readline().rstrip().split(',')

def dance(repetitions, moves):
    programs = []
    for i in range(97, 113, 1):
        programs.append(chr(i))
    seen = []
    seen.append(''.join(programs))
    for i in range(repetitions):
        # Dance
        for move in moves:
            # Spin?
            match = spinRegex.match(move)
            if match != None:
                rotations = int(match.group(1))
                programs = programs[(-1*rotations):] + programs[:(-1*rotations)]
                continue
            # Exchange?
            match = exchangeRegex.match(move)
            if match != None:
                pos1 = int(match.group(1))
                pos2 = int(match.group(2))
                temp = programs[pos1]
                programs[pos1] = programs[pos2]
                programs[pos2] = temp
                continue
            # Partner?
            match = partnerRegex.match(move)
            if match != None:
                pos1 = programs.index(match.group(1))
                pos2 = programs.index(match.group(2))
                temp = programs[pos1]
                programs[pos1] = programs[pos2]
                programs[pos2] = temp
                continue
            print('Regex missed: ' + move)
        # See if current order has been seen already
        currentOrder = ''.join(programs)
        if currentOrder in seen:
            return seen[repetitions % len(seen)]
        else:
            seen.append(currentOrder)
    return ''.join(programs)

print(dance(1, copy.copy(moves)))
print(dance(1000000000, copy.copy(moves)))
