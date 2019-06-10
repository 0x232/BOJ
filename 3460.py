for _ in range(int(input())):
    n = int(input())
    result = []
    i = 0
    while n > 0:
        if n % 2 == 1:
            result.append(i)
        n = n // 2
        i += 1
    print(' '.join(map(str, result)))
