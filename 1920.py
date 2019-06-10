N = int(input())
arr = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
arr.sort()
for i in range(M):
    low, high = 0, N-1
    flag = False
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == m[i]:
            flag = True
            break
        elif arr[mid] < m[i]:
            low = mid+1
        else:
            high = mid-1
    print(int(flag))
