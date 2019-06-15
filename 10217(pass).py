import sys
import heapq
# Consider cost condition.
for _ in range(int(sys.stdin.readline())):
    N, M, K = map(int, sys.stdin.readline().split())
    edge = {v: [] for v in range(1, N+1)}
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        edge[u].append([v, c, d])
    
    distance = [sys.maxsize]*(N+1)
    distance[1] = 0
    cost = [0]*(N+1)
    cost[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        d, v = heapq.heappop(pq)
        for e in edge[v]:
            u, c, w = e[0], e[1], e[2]
            if distance[u] > d + w:
                distance[u] = d + w
                cost[u] = cost[v] + c
                heapq.heappush(pq, (d + w, u))
    print(cost[N] if cost[N] < M else 'Poor KCM')
