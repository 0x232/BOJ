import itertools


def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for _ in range(int(input())):
    n = list(map(int, input().split()))
    print(sum(GCD(a, b) for a, b in itertools.combinations(n[1:], 2)))
