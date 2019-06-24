for _ in range(3):
    result = list(map(input().count, '01'))
    if result[0] == 1:
        print('A')
    elif result[0] == 2:
        print('B')
    elif result[0] == 3:
        print('C')
    elif result[0] == 4:
        print('D')
    else:
        print('E')
