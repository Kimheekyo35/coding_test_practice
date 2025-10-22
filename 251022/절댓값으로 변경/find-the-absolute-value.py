n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def make_upper(k):
    return abs(k)

for i in range(n):
    if arr[i] < 0:
        arr[i] = make_upper(arr[i])

print(*arr)
