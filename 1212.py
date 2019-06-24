converter = ['000', '001', '010', '011',
             '100', '101', '110', '111']
for i, s in enumerate(input()):
    n = int(s)
    if i > 0:
        print(converter[n], end='')
    else:
        if n < 2:
            print(converter[n][2], end='')
        elif n < 4:
            print(converter[n][1:], end='')
        else:
            print(converter[n], end='')
