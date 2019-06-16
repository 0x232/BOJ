import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

d = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if d[a-1][b-1] > c:
        d[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            print(d)
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

# INF=>0 (for print)
for i in range(n):
    for j in range(n):
        if d[i][j] == sys.maxsize:
            d[i][j] = 0

for i in range(n):
    print(' '.join(map(str, d[i])))
