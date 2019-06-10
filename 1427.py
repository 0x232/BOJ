def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less = []
    more = []
    equal = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            more.append(x)
        else:
            equal.append(x)
    return quick_sort(more) + equal + quick_sort(less)
arr = []
for i in input():
    arr.append(int(i))
for i in quick_sort(arr):
    print(i, end='')
