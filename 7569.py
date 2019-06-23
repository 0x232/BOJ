import sys
import collections

M, N, H = map(int, sys.stdin.readline().split())
box = [[sys.stdin.readline().split() for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

queue = collections.deque([])
number_of_tomato = M*N*H
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == '1':
                queue.append((i, j, k, 0))
            if box[i][j][k] == '-1':
                number_of_tomato -= 1

direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0),
             (0, 1, 0), (0, 0, -1), (0, 0, 1)]
days_to_ripen = 0

while queue:
    h, r, c, days_to_ripen = queue.popleft()
    number_of_tomato -= 1
        for i, j, k in direction:
        nh, nr, nc = h+i, r+j, c+k
        if nh >= 0 and nr >= 0 and nc >= 0 and \
           nh < H and nr < N and nc < M and \
           not visited[nh][nr][nc] and \
           box[nh][nr][nc] == '0':
            queue.append((nh, nr, nc, days_to_ripen+1))
            visited[nh][nr][nc] = True

print(days_to_ripen if number_of_tomato == 0 else -1)
