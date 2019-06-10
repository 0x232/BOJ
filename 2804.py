A, B = input().split()
s = set(A) & set(B)
a, b = 0, 0
c = ''
for i in range(len(A)):
    if A[i] in s:
        a = i
        c = A[i]
        break
for i in range(len(B)):
    if B[i] == c:
        b = i
        break
for j in range(len(B)):
    for i in range(len(A)):
        if i == a:
            print(B[j], end='')
        elif j == b:
            print(A[i], end='')
        else:
            print('.', end='')
    print('')
