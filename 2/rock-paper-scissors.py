input = open("input.txt", "r")

options = ['X', 'Y', 'Z']

totalScore = 0

for line in input:
    c1 = line[0]
    c2 = line[2]

    c1Index = (ord(c1) - 65)
    c2Index = (ord(c2) - 88)

    result = (c1Index - c2Index) % 3

    # extra points for
    extraPoints = c2Index + 1
    totalScore += extraPoints

    totalScore += 6 if result == 2 else 0 if result == 1 else 3

print(totalScore)
