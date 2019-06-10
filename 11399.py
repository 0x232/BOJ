import sys
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
time = 0
for i in range(n):
    time += p[i]*(n-i)
print(time)
