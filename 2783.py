X, Y = map(int, input().split())
price = X/Y
for _ in range(int(input())):
    Xi, Yi = map(int, input().split())
    if Xi/Yi < price:
        price = Xi/Yi

print(price*1000)
