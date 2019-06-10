order = []
for _ in range(int(input())):
    order.append(int(input()))
arr = sorted(order)
stack = []
operation = ''
while True:
    if not order:
        break
    if not stack:
        stack.append(arr.pop(0))
        operation += '+'
    if stack[-1] == order[0]:
        stack.pop()
        order.pop(0)
        operation += '-'
    elif stack[-1] < order[0]:
        stack.append(arr.pop(0))
        operation += '+'
    else:
        operation = ''
        break
if not operation:
    print('NO')
else:
    for i in operation:
        print(i)
        
