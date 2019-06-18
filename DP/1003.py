import sys
T = int(sys.stdin.readline())
fib = []
fib.append([1,0])
fib.append([0,1])
for i in range(2, 41):
    fib.append([fib[i-2][0]+fib[i-1][0], fib[i-2][1]+fib[i-1][1]])
for _ in range(T):
    N = int(sys.stdin.readline())
    print(fib[N][0], fib[N][1])
