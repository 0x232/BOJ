from math import sqrt
def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
    return True

arr = list(range(1, 10001))
prime_number = list(map(prime, arr))

for _ in range(int(input())):
    n = int(input())
