import sys
import collections


def find_island(row, col, island_number):
    queue = collections.deque([(row, col)])
    grid[row][col] = island_number
    visited[row][col] = True
    while queue:
        r, c = queue.popleft()
        for i, j in direction:
            nr, nc = r+i, c+j
            if nr >= 0 and nr < N and nc >= 0 and nc < N and \
               grid[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc))
                grid[nr][nc] = island_number
                visited[nr][nc] = True


def reclaim_island(island_number):
    queue = collections.deque([])
    for i in range(N):
        for j in range(N):
            if grid[i][j] == island_number:
                queue.append((i, j, 0))

    while queue:
        r, c, distance = queue.popleft()
        for i, j in direction:
            nr, nc = r+i, c+j
            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                if grid[nr][nc] != 0 and grid[nr][nc] != island_number:
                    return distance
                if grid[nr][nc] == 0 and not visited[nr][nc]:
                    queue.append((nr, nc, distance+1))
                    visited[nr][nc] = True

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

island_number = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            island_number += 1
            find_island(i, j, island_number)

distance = sys.maxsize
for i in range(1, island_number):
    visited = [[False]*N for _ in range(N)]
    distance = min(distance, reclaim_island(i))

print(distance)
