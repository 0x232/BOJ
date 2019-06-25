# Better Solution:
# https://www.acmicpc.net/source/13139101

N = int(input())
cute = 0
for _ in range(N):
    if input() == '1':
        cute += 1
if cute > N//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
