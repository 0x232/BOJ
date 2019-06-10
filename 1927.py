import heapq
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)
    else:
        heapq.heappush(heap, x)