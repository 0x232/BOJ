stack = []
count = 0
total = 0
for paren in input():
    if paren == '(':
        stack.append(paren)
        count += 1
    else:
        # Laser
        if stack[-1] == '(':
            stack.append(paren)
            count -= 1
            total += count
        # Iron Rod
        else:
            stack.append(paren)
            count -= 1
            total += 1
print(total)
