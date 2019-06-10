import sys
# sys.stdin.read() reads until EOF.
text = sys.stdin.read()
arr = list(map(text.count, 'abcdefghijklmnopqrstuvwxyz'))
for i in range(len(arr)):
    if arr[i] == max(arr):
        print(chr(i+97), end='')
