file = []
for _ in range(int(input())):
    file.append(input())
s = list(file[0])
for i in range(1, len(file)):
    for j in range(len(s)):
        if s[j] != file[i][j]:
            s[j] = '?'
for c in s:
    print(c, end='')