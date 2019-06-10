N, M = map(int, input().split())
while N != 0 or M != 0:
    player = [0] * 10000
    for _ in range(N):
        for rank in map(int, input().split()):
            player[rank-1] += 1
    player[player.index(max(player))] = 0
    m = max(player)
    result = []
    for i in range(len(player)):
        if player[i] == m:
            result.append(i+1)
    print(' '.join(map(str, result)))
    N, M = map(int, input().split())
