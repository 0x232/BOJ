import sys

c = []
for _ in range(int(sys.stdin.readline())):
    c.append(tuple(map(int, sys.stdin.readline().split())))
c.sort()
for x, y in c:
    print(x, y)
