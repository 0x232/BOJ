import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

vertex = list(range(1, V+1))
edge = {v: [] for v in range(1, V+1)}
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u].append([v, w])

distance = {v: sys.maxsize for v in range(1, V+1)}
distance[K] = 0

while len(vertex) > 0:
    u = 0
    d = sys.maxsize
    for v in vertex:
        if d > distance[v]:
            u = v
            d = distance[v]

    if d == sys.maxsize:
        break

    vertex.remove(u)

    for e in edge[u]:
        v, w = e[0], e[1]
        distance[v] = min(distance[v], distance[u] + w)

for v in range(1, V+1):
    print('INF' if distance[v] == sys.maxsize else distance[v])
