import collections


def BFS(row, col, color):
    q = collections.deque([(row, col)])
    visited[row][col] = True
    while q:
        r, c = q.popleft()
        for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
            if r+i >= 0 and r+i < N and c+j >= 0 and c+j < N and \
               not visited[r+i][c+j] and \
               grid[r+i][c+j] == color:
                q.append((r+i, c+j))
                visited[r+i][c+j] = True

N = int(input())
grid = [input() for _ in range(N)]
visited = [[False]*N for _ in range(N)]

number_of_area = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j, grid[i][j])
            number_of_area += 1
print(number_of_area, end=' ')

for i in range(N):
    grid[i] = grid[i].replace('G', 'R')
    visited[i] = [False]*N

number_of_area = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j, grid[i][j])
            number_of_area += 1
print(number_of_area)
