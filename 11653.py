def factorize(N):
    i = 2
    while N > 1:
        if N % i != 0:
            i += 1
        else:
            N = N // i
            print(i)

factorize(int(input()))
