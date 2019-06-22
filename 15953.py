import sys
import math

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    prize_money = 0

    if a == 0 or a > 21:
        pass
    elif a == 1:
        prize_money += 5000000
    elif a < 4:
        prize_money += 3000000
    elif a < 7:
        prize_money += 2000000
    elif a < 11:
        prize_money += 500000
    elif a < 16:
        prize_money += 300000
    elif a < 22:
        prize_money += 100000

    if b > 0 and b < 32:
        b = int(math.log2(b)) + 1
        prize_money += 2**(10-b) * 10000

    print(prize_money)
