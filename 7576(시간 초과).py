import sys


def is_in_range(n, m, row, col):
    return row >= 0 and row < n and col >= 0 and col < m


def BFS(n, m, row, col, number_of_ripe_tomato):
    # Initialization.
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

    q = [(row, col)]
    visited[row][col] = True
    days_to_ripen[row][col] = 0
    while q:
        r, c = q.pop(0)
        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            if is_in_range(n, m, r+dr, c+dc) and \
               box[r+dr][c+dc] == '0' and \
               not visited[r+dr][c+dc]:
                q.append((r+dr, c+dc))
                visited[r+dr][c+dc] = True
                if number_of_ripe_tomato > 1:
                    days_to_ripen[r+dr][c+dc] = \
                        min(days_to_ripen[r+dr][c+dc], days_to_ripen[r][c]+1)
                else:
                    days_to_ripen[r+dr][c+dc] = days_to_ripen[r][c] + 1

M, N = map(int, sys.stdin.readline().split())
box, visited, days_to_ripen = [], [], []
for _ in range(N):
    box.append(sys.stdin.readline().split())
    visited.append([False]*M)
    days_to_ripen.append([-1]*M)

number_of_ripe_tomato = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == '1':
            number_of_ripe_tomato += 1
            BFS(N, M, i, j, number_of_ripe_tomato)

box = [x for l in box for x in l]
days_to_ripen = [x for l in days_to_ripen for x in l]
if box.count('-1') < days_to_ripen.count(-1):
    print(-1)
else:
    print(max(days_to_ripen))
