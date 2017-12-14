
import os
import os.path
import re

regex = re.compile(r'(\d+)\s<->\s(.*)')

programPipes = {}

programsWithGroup = set()

groups = 0

# Get all of the programs and their pipes
with open(os.path.join(os.getcwd(), 'Day12', 'input.txt'), 'r') as input:
    for line in input:
        match = regex.match(line.rstrip())
        program = match.group(1)
        pipes = match.group(2).replace(' ', '').split(',')
        programPipes[program] = pipes

# Explore program pipes
# Iterate through all programs
for program in programPipes.keys():
    # Check to see if this program is in a group already
    if program in programsWithGroup:
        continue
    # Explore this program
    programsInThisGroup = set()
    explored = set()
    frontier = set()
    frontier.add(program)
    while len(frontier) > 0:
        # Get the next program to inspect
        currentProgram = frontier.pop()
        explored.add(currentProgram)
        for pipe in programPipes[currentProgram]:
            programsInThisGroup.add(pipe)
            if pipe not in explored:
                frontier.add(pipe)
    # Add all the programs in this group to the
    # list of programs already found to be in a group
    # So we don't try to explore them again
    for p in programsInThisGroup:
        programsWithGroup.add(p)
    groups += 1

print(str(groups))
    