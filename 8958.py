n = int(input())
for _ in range(n):
    result = input()
    score = []
    for i in range(len(result)):
        if not score:
            if result[i] == 'O':
                score.append(1)
            else:
                score.append(0)
        else:
            if result[i] == 'O':
                score.append(score[i-1]+1)
            else:
                score.append(0)
    print(sum(score))
