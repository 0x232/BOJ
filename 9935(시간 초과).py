import re
s = input()
bomb = input()
p = re.compile(bomb)
while p.search(s):
    s = re.sub(bomb, '', s)
print(s if s else 'FRULA')
