import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

heapq.heapify(A)
num = 0
for i in range(K):
    num = heapq.heappop(A)
print(num)
