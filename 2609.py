def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def LCM(a, b):
    return a * b // GCD(a, b)

a, b = map(int, input().split())
print(GCD(a, b))
print(LCM(a, b))
