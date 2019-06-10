def lcp(a, b):
    prefix = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            prefix += 1
        else:
            break
    return prefix

string = input()
suffix = []
for i in range(len(string)):
    suffix.append([string[i:], i+1])
suffix.sort(key=lambda x: x[0])
lcp_array = ['x']
for i in range(1, len(suffix)):
    lcp_array.append(lcp(suffix[i-1][0], suffix[i][0]))

for x in suffix:
    print(x[1], end=' ')
print('')
for x in lcp_array:
    print(x, end=' ')
