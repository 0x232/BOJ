import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    five = 0
    i = 5
    while i <= N:
        five += N // i
        i *= 5
    print(five)