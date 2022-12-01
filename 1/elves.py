input = open("input.txt", "r")

largest = [0, 0, 0]
acc = 0
for line in input:
    if line == "\n":
        largest.sort()
        largest[0] = acc if acc > largest[0] else largest[0]
        acc = 0
    else:
        acc += int(line)

print("Largest three elves:", largest)

sum = 0
for val in largest:
    sum += val

print("Sum of calories:", sum)
