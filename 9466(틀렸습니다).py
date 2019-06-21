def find_cycle(u, v):
    if visited[v]:
        return u == v
    else:
        visited[v] = True
        return find_cycle(u, edge[v])

edge = [0] * (100001)
visited = [False] * (100001)

for _ in range(int(input())):
    n = int(input())
    i = 1
    for x in list(map(int, input().split())):
        edge[i] = x
        visited[i] = False
        i += 1

    print(sum(1 for i in range(1, n+1) if not find_cycle(i, i)))
