import sys


# Recursion is slightly faster than iteration.
def bisect(low, high, answer):
    if low > high:
        return answer
    mid = (low + high) // 2
    total = sum(i//mid for i in cable)
    if total >= N:
        return bisect(mid+1, high, mid)
    else:
        return bisect(low, mid-1, answer)

K, N = map(int, sys.stdin.readline().split())
cable = []
for _ in range(K):
    cable.append(int(sys.stdin.readline())) 
print(bisect(1, max(cable), 0))
