n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n-1):
    for j in range(i,n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

[print(f,end=' ') for f in arr]