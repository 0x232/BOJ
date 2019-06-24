number = [int(input()) for _ in range(9)]
total = sum(number)
for i in range(9):
    for j in range(9):
        if total - number[i] - number[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(number[k])
            break
