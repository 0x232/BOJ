N = int(input())
i = 1
while True:
    s = i*(i+1)//2
    if s > N:
        print(i-1)
        break
    i += 1
