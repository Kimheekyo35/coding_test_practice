N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
total = 0
for i in range(N):
    total += arr[i]
    if arr[i]> abs(total-S):
        break
print(abs(total-S))