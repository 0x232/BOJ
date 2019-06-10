n, k = map(int, input().split())
arr = list(range(2, n+1))
count = 1
while count <= k:
    prime = arr[0]
    for x in arr:
        if x % prime == 0:
            if count == k:
                print(x)
            arr.remove(x)
            count += 1