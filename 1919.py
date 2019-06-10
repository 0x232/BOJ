a = 'abcdefghijklmnopqrstuvwxyz'
a1 = list(map(input().count, a))
a2 = list(map(input().count, a))
print(sum(abs(i1-i2) for i1, i2 in zip(a1, a2)))
