import sys
import heapq
meeting = []
for _ in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(meeting,(end, start))

count = 0
while meeting:
    end = heapq.heappop(meeting)[0]
    count += 1
    while meeting and meeting[0][1] < end:
        heapq.heappop(meeting)

print(count)
