import itertools

number = [int(input()) for _ in range(9)]
for x in itertools.combinations(number, 7):
    if sum(x) == 100:
        print('\n'.join(map(str, x)))
        break
