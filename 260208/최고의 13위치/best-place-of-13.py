n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0

for i in range(n):
    for j in range(n-2):
        cnt = 0
        for k in range(3):
            if grid[i][j+k] == 1:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
        