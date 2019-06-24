import collections

R, C = map(int, input().split())
grid = [list(map(lambda x: x, input())) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = collections.deque([])
for i in range(R):
    for j in range(C):
        if grid[i][j] == '*':
            queue.appendleft(('*', i, j, 0))
            visited[i][j] = True
        if grid[i][j] == 'D':
            queue.append(('D', i, j, 0))
            visited[i][j] = True

result = 'KAKTUS'
while queue:
    g, r, c, t = queue.popleft()
    for i, j in direction:
        nr, nc = r+i, c+j
        if nr >= 0 and nr < R and nc >= 0 and nc < C:
            if g == 'D' and grid[nr][nc] == 'S':
                result = t+1
                break
        # if nr >= 0 and nr < R and nc >= 0 and nc < C and \
            if grid[nr][nc] == '.' and not visited[nr][nc]:
                queue.append((g, nr, nc, t+1))
                visited[nr][nc] = True
                if g == '*':
                    grid[nr][nc] = '*'
    print(r, c)
    for i in range(R):
        print(''.join(grid[i]))
print(result)
'''
for i in range(R):
    print(''.join(grid[i]))
'''
