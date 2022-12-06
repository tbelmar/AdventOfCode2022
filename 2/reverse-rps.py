input = open("input.txt", "r")

totalScore = 0

for line in input:
    p1 = line[0]
    c2 = line[2]

    p1Index = (ord(p1) - 65)
    c2Index = (ord(c2) - 88)
    p2Index = (p1Index + 2 - 2*c2Index) % 3

    # 'X' = 0pts, 'Y' = 3pts, 'Z' = 6pts
    extraPoints = 3 * c2Index
    totalScore += extraPoints

    totalScore += p2Index + 1

print(totalScore)
