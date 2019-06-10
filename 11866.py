N, K = map(int, input().split())
arr = list(range(1, N+1))
seq = []
while arr:
    for _ in range(K-1):
        arr.append(arr.pop(0))
    seq.append(arr.pop(0))
print('<' + ', '.join(map(str, seq)) + '>')
