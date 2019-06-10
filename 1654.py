import sys

K, N = map(int, sys.stdin.readline().split())
cable = []
for _ in range(K):
    cable.append(int(sys.stdin.readline()))
low, high = 1, max(cable)
answer = 0
while low <= high:
    mid = (low + high) // 2
    total = sum(i//mid for i in cable)
    if total >= N:
        answer = mid
        low = mid + 1
    if total < N:
        high = mid - 1
print(answer)
