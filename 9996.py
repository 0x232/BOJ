import re
N = int(input())
pattern = input().split('*')
p = re.compile(pattern[0] + '[a-z]*' + pattern[1] + '$')
for _ in range(N):
    print('DA' if p.match(input()) else 'NE')
