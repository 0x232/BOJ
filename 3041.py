distance = 0
for i in range(4):
    puzzle = input()
    for j in range(4):
        if puzzle[j] == '.':
            continue
        idx = ord(puzzle[j]) - 65
        distance += abs(i - idx // 4) + abs(j - idx % 4)
print(distance)
