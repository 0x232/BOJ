import sys
import heapq

heap = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            _, v = heapq.heappop(heap)
            print(v)
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))