train = [0]
for i in range(4):
    a, b = map(int, input().split())
    train.append(train[i]-a+b)
print(max(train))
