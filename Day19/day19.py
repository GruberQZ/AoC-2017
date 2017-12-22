import os
import os.path

def go():
    # Build grid
    grid = []
    input = open(os.path.join(os.getcwd(), 'Day19', 'input.txt'))
    for line in input:
        grid.append(list(line.replace('\n', '')))
    grid.append([' '] * len(grid[0]))

    letters = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    path = []

    # Find the starting position in the first row
    pos = [0, grid[0].index('|')]
    direction = [1, 0]
    count = 0
    while True:
        count += 1
        # Check the character at the current position
        char = grid[pos[0]][pos[1]]
        # Track order of letters seen
        if char in letters:
            path.append(char)
        # Figure out the next position
        nextPos = [pos[0] + direction[0], pos[1] + direction[1]]
        # Can we keep going in the same direction?
        if grid[nextPos[0]][nextPos[1]] != ' ':
            pos = nextPos
            continue
        # Have to switch directions
        # Must go 90 degrees from current direction
        if direction[1] != 0:
            # Figure out of if we should go left or right
            if grid[pos[0] + 1][pos[1]] != ' ':
                direction = [1, 0]
            elif grid[pos[0] - 1][pos[1]] != ' ':
                direction = [-1, 0]
            else:
                return path, count
        else:
            # Figure out of if we should go up or down
            if grid[pos[0]][pos[1] + 1] != ' ':
                direction = [0, 1]
            elif grid[pos[0]][pos[1] - 1] != ' ':
                direction = [0, -1]
            else:
                return path, count
        # Compute next position
        pos = [pos[0] + direction[0], pos[1] + direction[1]]

path, steps = go()
print(''.join(path))
print(str(steps))
