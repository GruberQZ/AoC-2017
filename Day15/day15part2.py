
prevA = 679
prevB = 771

factorA = 16807
factorB = 48271

count = 0
for i in range(5000000):
    # Get next A
    # if i % 50 == 0:
    #     print(str(i))
    newA = (prevA * factorA) % 2147483647
    while newA % 4 != 0:
        prevA = newA
        newA = (prevA * factorA) % 2147483647
    # Get next B
    newB = (prevB * factorB) % 2147483647
    while newB % 8 != 0:
        prevB = newB
        newB = (prevB * factorB) % 2147483647
    if bin(newA).lstrip('-0b').zfill(16)[-16:] == bin(newB).lstrip('-0b').zfill(16)[-16:]:
        count += 1
    # Save values
    prevA = newA
    prevB = newB

print(str(count))

