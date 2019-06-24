for i, s in enumerate(input()):
    n_8 = int(s)
    n_2 = ''
    if n_8 == 0:
        n_2 = '0'
    while n_8 > 0:
        n_2 = str(n_8 % 2) + n_2
        n_8 = n_8 // 2
    if i > 0:
        n_2 = '0'*(3-len(n_2)) + n_2
    print(n_2, end='')