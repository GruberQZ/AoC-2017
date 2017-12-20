
def insert_into_buffer(steps):
    currentPosition = 0
    indexOf0 = 0
    bufferLength = 1
    valueAfter0 = 0
    for i in range(1, 50000000 + 1, 1):
    # for i in range(1, 100000, 1):
        # Get the new current position
        currentPosition = (currentPosition + steps) % bufferLength
        # If the current position is the index of 0,
        # Update the value after 0
        if currentPosition == indexOf0:
            valueAfter0 = i
        # Update length of list
        bufferLength += 1
        # Update current position to be position of newly
        # inserted list element
        if currentPosition == bufferLength - 1:
            currentPosition = 0
        else:
            currentPosition += 1
    return valueAfter0

print(str(insert_into_buffer(348)))
