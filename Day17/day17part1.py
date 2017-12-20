

def insert_into_buffer(steps):
    buffer = [0]
    lastBufferPos = 0
    currentPos = 0
    # Range to 2018 so last number is 2017
    for i in range(1, 2018):
        # Walk forward in the buffer steps times
        # Walk an extra step because we insert one space ahead
        for j in range(steps + 1):
            if currentPos == lastBufferPos:
                currentPos = 0
            else:
                currentPos += 1
        # Insert here
        buffer.insert(currentPos, i)
        # Increment last buffer position
        lastBufferPos += 1
    # Return value of index in front of current position
    if currentPos == lastBufferPos:
        return buffer[0]
    else:
        return buffer[currentPos + 1]

print(insert_into_buffer(348))