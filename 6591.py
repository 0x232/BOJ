n, k = map(int, input().split())
while n != 0 or k != 0:
    t = min(k, n-k)
    x, y = 1, 1
    while t > 0:
        x *= (n-t+1)
        y *= t
        t -= 1
    print(x//y)
    n, k = map(int, input().split())
