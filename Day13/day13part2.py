import os
import os.path
import re

regex = re.compile(r'(\d+):\s(\d+)')

layers = {}

with open(os.path.join(os.getcwd(), 'Day13', 'input.txt'), 'r') as input:
    for line in input:
        match = regex.match(line.rstrip())
        layerPosition = int(match.group(1))
        layerLength = int(match.group(2))
        layers[layerPosition] = layerLength

stillSearching = True
delay = 0
while stillSearching:
    # Not searching again unless we need to keep going
    stillSearching = False
    # Go through all the layers and figure out
    # if we'll be caught in any of the positions
    for layerPosition in layers:
        totalDelay = delay + layerPosition
        if totalDelay % (2 * (layers[layerPosition] - 1)) == 0:
            stillSearching = True
            break
    if not stillSearching:
        break
    # Increment
    delay += 1

print(str(delay)) 