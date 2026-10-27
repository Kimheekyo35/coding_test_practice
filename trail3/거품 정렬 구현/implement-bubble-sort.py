n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
temp = 0
sorted = True
i = 0

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

[print(i,end=' ') for i in arr]

