import sys
import collections


def is_in_range(H, N, M, h, r, c):
    return h >= 0 and r >= 0 and c >= 0 and \
           h < H and r < N and c < M

M, N, H = map(int, sys.stdin.readline().split())
box = [[] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        box[i].append(sys.stdin.readline().split())

queue = collections.deque([])
number_of_tomato = M*N*H
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == '1':
                queue.append((i, j, k, 0))
            if box[i][j][k] == '-1':
                number_of_tomato -= 1

days_to_ripen = 0

while queue:
    h, r, c, days_to_ripen = queue.popleft()
    number_of_tomato -= 1
    direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0),
                 (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    for i, j, k in direction:
        if is_in_range(H, N, M, h+i, r+j, c+k) and \
           not visited[h+i][r+j][c+k] and \
           box[h+i][r+j][c+k] == '0':
            queue.append((h+i, r+j, c+k, days_to_ripen+1))
            visited[h+i][r+j][c+k] = True
            box[h+i][r+j][c+k] = '1'

print(days_to_ripen if number_of_tomato == 0 else -1)
