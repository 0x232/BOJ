import sys
rope = []
for _ in range(int(sys.stdin.readline())):
    rope.append(int(sys.stdin.readline()))
rope.sort(reverse=True)
w = 0
k = 0
for x in rope:
    if x*(k+1) > w:
        k += 1
        w = x*k
    else:
        k += 1
print(w)
    
