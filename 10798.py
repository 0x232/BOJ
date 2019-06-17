c = [['' for _ in range(15)] for _ in range(5)]
for i in range(5):
    s = input()
    for j in range(len(s)):
        c[i][j] = s[j]
for j in range(15):
    for i in range(5):
        print(c[i][j], end='')
