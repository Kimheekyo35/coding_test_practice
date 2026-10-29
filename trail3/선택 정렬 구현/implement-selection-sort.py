n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
tmp = 0

for i in range(n-1):
    for j in range(i+1,n):
        if arr[j] < arr[i]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

[print(i,end=" ") for i in arr]

