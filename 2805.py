import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
low, high = 0, max(tree)
answer = 0
while low <= high:
    mid = (low+high)//2
    total = sum(i-mid if i > mid else 0 for i in tree)
    if total > M:
        answer = mid
        low = mid + 1
    if total < M:
        high = mid - 1
    if total == M:
        answer = mid
        break
print(answer)
