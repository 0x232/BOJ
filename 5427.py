import collections

for _ in range(int(input())):
    w, h = map(int, input().split())
    grid = [[x for x in input()] for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    queue = collections.deque([])
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '*':
                queue.append((i, j, 0))
            if grid[i][j] == '#':
                visited[i][j] = True
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                queue.append((i, j, 0))
                break

    escape = False
    while queue:
        r, c, time = queue.popleft()
        if r == 0 or r == h-1 or c == 0 or c == w-1:
            if grid[r][c] == '@':
                escape = True
                print(time+1)
                break
        for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
            if r+i >= 0 and r+i < h and c+j >= 0 and c+j < w and \
               not visited[r+i][c+j] and grid[r+i][c+j] == '.':
                queue.append((r+i, c+j, time+1))
                visited[r+i][c+j] = True
                grid[r+i][c+j] = grid[r][c]
    if not escape:
        print('IMPOSSIBLE')
