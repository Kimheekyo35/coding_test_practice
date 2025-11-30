n = int(input())
arr = [int(input()) for _ in range(n)]

cnt, max_cnt = 0, 0

for i in range(n):
    if i == 0 or (arr[i]-arr[i-1] > 0):
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)


# cnt, max_cnt = 1, 1
# for i in range(1,n):
# 이렇게 cnt도 1로 초기화헤야 둘이 같은 코드가 됨