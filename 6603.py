import itertools

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    for c in itertools.combinations(s[1:], 6):
        print(' '.join(map(str, c)))
    print('')
