n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    temp = 0
    if arr[i] % 2 == 0:
        temp = arr[i] // 2
        arr[i] = temp
    else:
        pass

print(*arr)
    