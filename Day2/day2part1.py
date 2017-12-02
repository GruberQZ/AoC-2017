
file = open('d:\AoC-2017\Day2\input.txt', 'r')

total = 0

for row in file:
    data = list(int(x) for x in row.rstrip().split("\t"))
    smallest = data[0]
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
        elif data[i] > largest:
            largest = data[i]
    total += (largest - smallest)

print(str(total))

