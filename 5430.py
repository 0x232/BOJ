import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline()
    arr_len = int(sys.stdin.readline())
    arr = sys.stdin.readline()
    d = deque([])
    if arr_len != 0:
        d = deque(map(int, arr[1:-2].split(',')))

    r = 0
    flag = False
    for c in command:
        if c == 'R':
            r += 1
        if c == 'D':
            if len(d) == 0:
                flag = True
                break
            else:
                if r % 2 == 0:
                    d.popleft()
                else:
                    d.pop()

    if flag:
        print('error')
    else:
        if r % 2 == 1:
            d.reverse()
        print(str(list(d)).replace(' ', ''))
        