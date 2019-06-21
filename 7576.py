import sys
import collections


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m


def BFS(n, m, row, col, ripe_tomato):
    number_of_tomato = 0
    q = collections.deque(ripe_tomato)
    while q:
        r, c = q.popleft()
        number_of_tomato += 1
        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            if is_in_range(n, m, r+dr, c+dc) and \
               box[r+dr][c+dc] == '0' and \
               days_to_ripen[r+dr][c+dc] == -1:
                q.append((r+dr, c+dc))
                days_to_ripen[r+dr][c+dc] = days_to_ripen[r][c] + 1
    return number_of_tomato

M, N = map(int, sys.stdin.readline().split())
box, days_to_ripen = [], []
for _ in range(N):
    box.append(sys.stdin.readline().split())
    days_to_ripen.append([-1]*M)

number_of_tomato = N*M
ripe_tomato = []
for i in range(N):
    for j in range(M):
        if box[i][j] == '-1':
            number_of_tomato -= 1
        if box[i][j] == '1':
            ripe_tomato.append((i, j))
            days_to_ripen[i][j] = 0

if number_of_tomato == BFS(N, M, i, j, ripe_tomato):
    print(max(map(max, days_to_ripen)))
else:
    print(-1)