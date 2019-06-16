import sys

v = int(input())
e = int(input())

d = [[sys.maxsize for _ in range(v)] for _ in range(v)]
for i in range(v):
    d[i][i] = 0
for _ in range(e):
    v1, v2 = map(int, input().split())
    d[v1-1][v2-1] = 1
    d[v2-1][v1-1] = 1

for k in range(v):
    for i in range(v):
        for j in range(v):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

print(sum(1 if d[0][i] != 0 and d[0][i] != sys.maxsize else 0
          for i in range(v)))
