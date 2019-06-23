import sys
import collections

M, N, H = map(int, sys.stdin.readline().split())
box = [[['0']*M for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

queue = collections.deque([])
number_of_tomato = M*N*H
for i in range(H):
    for j in range(N):
        s = sys.stdin.readline().split()
        for k in range(M):
            if s[k] == '1':
                box[i][j][k] = s[k]
                queue.append((i, j, k, 0))
            if s[k] == '-1':
                box[i][j][k] = s[k]
                number_of_tomato -= 1

direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0),
             (0, 1, 0), (0, 0, -1), (0, 0, 1)]
days_to_ripen = 0

while queue:
    h, r, c, days_to_ripen = queue.popleft()
    number_of_tomato -= 1
    nh, nr, nc = h-1, r, c
    if nh >= 0:
        if box[nh][nr][nc] == '0' and not visited[nh][nr][nc]:
            queue.append((nh, nr, nc, days_to_ripen+1))
            visited[nh][nr][nc] = True
    nh, nr, nc = h+1, r, c
    if nh < H:
        if box[nh][nr][nc] == '0' and not visited[nh][nr][nc]:
            queue.append((nh, nr, nc, days_to_ripen+1))
            visited[nh][nr][nc] = True
    nh, nr, nc = h, r-1, c
    if nr >= 0:
        if box[nh][nr][nc] == '0' and not visited[nh][nr][nc]:
            queue.append((nh, nr, nc, days_to_ripen+1))
            visited[nh][nr][nc] = True
    nh, nr, nc = h, r+1, c
    if nr < N:
        if box[nh][nr][nc] == '0' and not visited[nh][nr][nc]:
            queue.append((nh, nr, nc, days_to_ripen+1))
            visited[nh][nr][nc] = True
    nh, nr, nc = h, r, c-1
    if nc >= 0:
        if box[nh][nr][nc] == '0' and not visited[nh][nr][nc]:
            queue.append((nh, nr, nc, days_to_ripen+1))
            visited[nh][nr][nc] = True
    nh, nr, nc = h, r, c+1
    if nc < M:
        if box[nh][nr][nc] == '0' and not visited[nh][nr][nc]:
            queue.append((nh, nr, nc, days_to_ripen+1))
            visited[nh][nr][nc] = True

print(days_to_ripen if number_of_tomato == 0 else -1)
