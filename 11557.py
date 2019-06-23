for _ in range(int(input())):
    S, L = [], []
    for _ in range(int(input())):
        name, drink = input().split()
        S.append(name)
        L.append(int(drink))
    print(S[L.index(max(L))])
