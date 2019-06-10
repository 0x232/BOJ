s = input()
bomb = input()
while bomb in s:
    s = s.replace(bomb, '', 1)
if not s:
    print('FRULA')
else:
    print(s)