import sys
n = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(n):
    arr[int(sys.stdin.readline())] += 1
for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)
