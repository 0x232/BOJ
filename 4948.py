from math import sqrt
def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
    return True

arr = list(range(1, 123456*2+1))
prime_number = list(filter(prime, arr))

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(1 for x in prime_number if x>n and x<=2*n))
