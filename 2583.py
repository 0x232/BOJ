import collections


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m


def BFS(n, m, row, col):
    q = collections.deque([(row, col)])
    visited[row][col] = True
    size_of_area = 1
    while q:
        r, c = q.popleft()
        for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
            if is_in_range(n, m, r+i, c+j) and \
               not visited[r+i][c+j] and \
               grid[r+i][c+j] == 0:
                q.append((r+i, c+j))
                visited[r+i][c+j] = True
                size_of_area += 1
    return size_of_area

M, N, K = map(int, input().split())
grid = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[M-1-y][x] = 1

number_of_area = 0
size_of_area = []
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            number_of_area += 1
            size_of_area.append(BFS(M, N, i, j))

print(number_of_area)
print(' '.join(map(str, sorted(size_of_area))))
