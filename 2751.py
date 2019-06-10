import sys
import heapq
heap = []
for _ in range(int(sys.stdin.readline())):
    heapq.heappush(heap, int(sys.stdin.readline()))
for _ in range(len(heap)):
    print(heapq.heappop(heap))