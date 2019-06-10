import sys

sys.setrecursionlimit(10**6)


def dp(D, order, W):
    if time[W-1] != -1:
        return time[W-1]
    if not order[W]:
        time[W-1] = D[W-1]
    else:
        max_value = 0
        for i in order[W]:
            max_value = max(dp(D, order, i), max_value)
        time[W-1] = D[W-1] + max_value
    return time[W-1]

for _ in range(int(sys.stdin.readline())):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    order = {key: [] for key in range(1, N+1)}
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        order[Y].append(X)
    W = int(sys.stdin.readline())
    time = [-1] * N
    print(dp(D, order, W))
