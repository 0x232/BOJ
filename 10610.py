a = list(input())
a.sort()
if sum(map(int, a)) % 3 == 0 and a[0] == '0':
    print(''.join(a[::-1]))
else:
    print(-1)
