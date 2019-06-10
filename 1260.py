# TODO: optimize code
N, M, V = map(int, input().split())
e = {key: [] for key in range(1, N+1)}
for _ in range(M):
    v1, v2 = map(int, input().split())
    e[v1].append(v2)
    e[v2].append(v1)
for i in e.keys():
    e[i] = sorted(e[i])
# DFS
visited = [False] * (N+1)
stack = [V]
dfs = []
while stack:
    v = stack.pop()
    if not visited[v]:
        dfs.append(v)
        visited[v] = True
    for x in reversed(e[v]):
        if not visited[x]:
            stack.append(x)
# BFS
visited = [False] * (N+1)
queue = [V]
visited[V] = True
bfs = []
while queue:
    v = queue.pop(0)
    bfs.append(v)
    for x in e[v]:
        if not visited[x]:
            queue.append(x)
            visited[x] = True

print(' '.join(map(str, dfs)) + '\n' + ' '.join(map(str, bfs)))
