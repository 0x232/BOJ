import collections


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m


def BFS(n, m, row, col):
    queue = collections.deque([(row, col)])
    distance[row][col] = 1
    while queue:
        r, c = queue.popleft()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            if is_in_range(n, m, r+dr[i], c+dc[i]) and \
               distance[r+dr[i]][c+dc[i]] == -1 and \
               maze[r+dr[i]][c+dc[i]] == '1':
                queue.append((r+dr[i], c+dc[i]))
                distance[r+dr[i]][c+dc[i]] = distance[r][c] + 1

maze = []
distance = []

N, M = map(int, input().split())
for _ in range(N):
    maze.append(input())
    distance.append([-1] * M)

BFS(N, M, 0, 0)
print(distance[N-1][M-1])
