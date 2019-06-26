import sys

for _ in range(int(sys.stdin.readline())):
    Yonsei, Korea = 0, 0
    for _ in range(9):
        a, b = map(int, sys.stdin.readline().split())
        Yonsei += a
        Korea += b
    if Yonsei == Korea:
        print('Draw')
    else:
        print('Yonsei' if Yonsei > Korea else 'Korea')
