for _ in range(int(input())):
    sound = input().split()
    animal = []
    s = input()
    while s != 'what does the fox say?':
        animal.append(s.split()[2])
        s = input()
    for x in sound:
        if x not in animal:
            print(x, end=' ')