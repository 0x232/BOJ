N = list(map(int, list(input())))
if N.count(0) > 0 and sum(N) % 3 == 0:
    N.sort(reverse=True)
    print(''.join(map(str, N)))
else:
    print(-1)
