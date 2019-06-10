def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True
n = int(input())
arr = list(map(int, input().split()))
print(list(filter(prime, arr)))
print(len(list(filter(prime, arr))))
