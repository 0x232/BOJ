N = int(input())
A = sorted(list(map(int, input().split())))
if N == 1:
    print(A[0]**2)
else:
    print(A[0]*A[-1])
