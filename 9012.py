n = int(input())
for _ in range(n):
    paren = input()
    counter = 0
    answer = True
    for p in paren:
        if counter < 0:
            answer = False
            break
        if p == '(':
            counter += 1
        if p == ')':
            counter -= 1
    if counter != 0:
        answer = False
    if answer:
        print('YES')
    else:
        print('NO')
