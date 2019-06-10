from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for l in range(1, N+1):
    for c in combinations(arr, l):
        if sum(c) == S:
            count += 1
print(count)
