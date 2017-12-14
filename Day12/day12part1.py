
import os
import os.path
import re

regex = re.compile(r'(\d+)\s<->\s(.*)')

programPipes = {}

frontier = set()

explored = set()

programsThatCanReach0 = set()

# Get all of the programs and their pipes
with open(os.path.join(os.getcwd(), 'Day12', 'input.txt'), 'r') as input:
    for line in input:
        match = regex.match(line.rstrip())
        program = match.group(1)
        pipes = match.group(2).replace(' ', '').split(',')
        programPipes[program] = pipes

# Explore program pipes
frontier.add('0')
while len(frontier) > 0:
    # Get the next program to inspect
    currentProgram = frontier.pop()
    explored.add(currentProgram)
    for pipe in programPipes[currentProgram]:
        programsThatCanReach0.add(pipe)
        if pipe not in explored:
            frontier.add(pipe)

print(str(len(programsThatCanReach0)))
    