import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
edge = {v: [] for v in range(1, V+1)}
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u].append([v, w])

distance = [sys.maxsize]*(V+1)
distance[K] = 0
pq = []
heapq.heappush(pq, (0, K))

while pq:
    d, u = heapq.heappop(pq)

    for e in edge[u]:
        v, w = e[0], e[1]
        if d + w < distance[v]:
            distance[v] = d + w
            heapq.heappush(pq, (d + w, v))

for v in range(1, V+1):
    print('INF' if distance[v] == sys.maxsize else distance[v])
