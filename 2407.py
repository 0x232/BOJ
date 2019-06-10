def f(n):
    if n < 1:
        return 1
    else:
        return n*f(n-1)

n, m = map(int, input().split())

print(f(n)//(f(m)*f(n-m)))
