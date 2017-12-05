
import os

input = open(os.getcwd() + '\Day4\input.txt')

total = 0

for line in input:
    words = line.rstrip().split(" ")
    uniqueWords = set()
    for word in words:
        uniqueWords.add(word)
    if len(uniqueWords) == len(words):
        total += 1

print(str(total))
