import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    prize_money = 0

    if a == 1:
        prize_money += 5000000
    if a > 1 and a < 4:
        prize_money += 3000000
    if a > 3 and a < 7:
        prize_money += 2000000
    if a > 6 and a < 11:
        prize_money += 500000
    if a > 10 and a < 16:
        prize_money += 300000
    if a > 15 and a < 22:
        prize_money += 100000

    if b > 0 and b < 32:
        b = int(math.log2(b)) + 1
        prize_money += 2**(10-b) * 10000

    print(prize_money)
