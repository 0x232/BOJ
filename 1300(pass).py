N = int(input())
k = int(input())
arr = [(i//N+1)*(i % N+1) for i in range(N*N)]
arr.sort()
print(arr[k-1])
