import sys
N, M = map(int, sys.stdin.readline().split())
arr1, arr2 = [], []
for _ in range(N):
    arr1.append(sys.stdin.readline()[:-1])
for _ in range(M):
    arr2.append(sys.stdin.readline()[:-1])
# Set operation is faster than in operation.
arr = sorted(list(set(arr1) & set(arr2)))
print(len(arr))
for x in arr:
    print(x)
