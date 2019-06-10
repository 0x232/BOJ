from math import sqrt
def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
    return True
m, n = map(int, input().split())
for i in range(m, n+1):
    if prime(i):
        print(i)
