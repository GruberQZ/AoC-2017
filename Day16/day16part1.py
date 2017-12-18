
import os
import os.path
import re

spinRegex = re.compile(r's(\d+)')
exchangeRegex = re.compile(r'x(\d+)\/(\d+)')
partnerRegex = re.compile(r'p(\w+)\/(\w+)')

programs = []

for i in range(97, 113, 1):
    programs.append(chr(i))

with open(os.path.join(os.getcwd(), 'Day16', 'input.txt'), 'r') as input:
    moves = input.readline().rstrip().split(',')
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

print(''.join(programs))