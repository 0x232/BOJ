puzzle = [list(input()) for _ in range(4)]
distance = 0
for i in range(4):
    for j in range(4):
        if puzzle[i][j] == '.':
            continue
        idx = ord(puzzle[i][j])-65
        distance += abs(i - (idx // 4)) + abs(j - (idx % 4))
print(distance)
