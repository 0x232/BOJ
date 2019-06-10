stick = [64]
X = int(input())
while sum(stick) > X:
    stick.append(stick.pop()//2)
    if sum(stick) < X:
        stick.append(stick[-1])
print(len(stick))
