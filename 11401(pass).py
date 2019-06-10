from math import sqrt

def prime(n):
    """Return whether n is prime or not."""
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def sieve(n):
    """Yield prime numbers less than n."""
    a = [True] * n
    a[0] = a[1] = False
    for (num, is_prime) in enumerate(a):
        if is_prime:
            yield num
            for i in range(2*num, n, num):
                a[i] = False

def num(x, p):
    """Return the number of p in factorized x."""
    i = 0
    while x % p == 0:
        i += 1
        x = x // p
    return i

N, K = map(int, input().split())
K  = min(K, N-K)
prime_number = [x for x in sieve(N+1)]

