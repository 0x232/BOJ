import collections


def BFS(N, M, row, col):
    queue = collections.deque([(row, col)])
    visited[row][col] = True
    size = 1
    while queue:
        r, c = queue.popleft()
        for i, j in direction:
            nr, nc = r+i, c+j
            if nr >= 1 and nr <= N and nc >= 1 and nc <= M and \
               grid[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True
                size += 1
    return size

N, M, K = map(int, input().split())
grid = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    grid[r][c] = 1
visited = [[False]*(M+1) for _ in range(N+1)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

max_size = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if grid[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, BFS(N, M, i, j))

print(max_size)
