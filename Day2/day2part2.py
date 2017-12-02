
file = open('d:\AoC-2017\Day2\input.txt', 'r')

total = 0

for row in file:
    data = list(int(x) for x in row.rstrip().split("\t"))
    rowComplete = False
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if data[i] % data[j] == 0:
                total += int(data[i] / data[j])
                rowComplete = True
            elif data[j] % data[i] == 0:
                total += int(data[j] / data[i])
                rowComplete = True
        if rowComplete:
            break

print(str(total))
