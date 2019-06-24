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
        if grid[i][j] == 'S':
            queue.append(('S', i, j, 0))
            visited[i][j] = True

success, result = False, 'KAKTUS'
while queue:
    g, r, c, t = queue.popleft()
    for i, j in direction:
        nr, nc = r+i, c+j
        if nr >= 0 and nr < R and nc >= 0 and nc < C:
            if g == 'S' and grid[nr][nc] == 'D':
                success, result = True, t+1
                break
            if grid[nr][nc] == '.' and not visited[nr][nc]:
                queue.append((g, nr, nc, t+1))
                visited[nr][nc] = True
                if g == '*':
                    grid[nr][nc] = '*'
    if success:
        break

print(result)
