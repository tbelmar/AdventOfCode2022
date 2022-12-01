input = open("input.txt", "r")

largest = 0
acc = 0
for line in input:
    if line == "\n":
        largest = acc if acc > largest else largest
        acc = 0
    else:
        acc += int(line)

print(largest)
