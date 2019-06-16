import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
edge = {v: [] for v in range(1, V+1)}
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edge[A].append((B, C))
    edge[B].append((A, C))

mstSet = []
key_value = []
heapq.heappush(key_value, (0, 1))
weight = 0
while len(mstSet) < V:
    while True:
        kv, u = heapq.heappop(key_value)
        if u not in mstSet:
            break
    mstSet.append(u)
    weight += kv
    for v, c in edge[u]:
        heapq.heappush(key_value, (c, v))

print(weight)
