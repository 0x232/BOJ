def decorate(row, col, char, frame):
    grid[row][col] = char
    for i, j in direction:
        grid[row+i][col+j] = frame

word = input()
width = 4*len(word)+1
grid = [['.']*width for _ in range(5)]
direction = [(-2, 0), (-1, -1), (-1, 1), (0, -2),
             (0, 2), (1, -1), (1, 1), (2, 0)]

idx = 0
for col in range(2, width, 4):
    if (idx + 1) % 3 != 0:
        decorate(2, col, word[idx], '#')
    idx += 1

idx = 0
for col in range(2, width, 4):
    if (idx + 1) % 3 == 0:
        decorate(2, col, word[idx], '*')
    idx += 1

for i in range(5):
    print(''.join(grid[i]))
