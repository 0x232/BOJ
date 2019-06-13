s = input().split('-')
v = sum(map(int, s[0].split('+')))
for x in s[1:]:
    v -= sum(map(int, x.split('+')))
print(v)