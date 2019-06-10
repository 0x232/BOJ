def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True
m = int(input())
n = int(input())
arr = list(range(m, n+1))
prime_number = list(filter(prime, arr))
if not prime_number:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))
