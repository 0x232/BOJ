for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n%h == 0:
        y, x = h, n//h
    else:
        y, x = n%h, n//h+1
    if x < 10:
        print('{}0{}'.format(y, x))
    else:
        print('{}{}'.format(y, x))
