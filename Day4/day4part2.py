import os

input = open(os.getcwd() + '\Day4\input.txt')

total = 0

for line in input:
    words = line.rstrip().split(" ")
    uniqueWords = set()
    for word in words:
        letterList = [0] * 26
        for char in word:
            letterList[ord(char) - 97] += 1
        uniqueWords.add(tuple(letterList))
    if len(uniqueWords) == len(words):
        total += 1

print(str(total))
        
