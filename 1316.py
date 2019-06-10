import itertools
count = 0
for _ in range(int(input())):
    s = ''.join(ch for ch, _ in itertools.groupby(input()))
    s = ''.join(sorted(s))
    if max(len(list(l)) for _, l in itertools.groupby(s)) == 1:
        count += 1
print(count)
            
