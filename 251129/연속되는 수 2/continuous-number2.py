n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 0
max_cnt = 0
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt+1)

