MAX_K = 100000  

n = int(input())
# 칠하는 칸
a = [0] * (2 * MAX_K + 1)
# black, white가 
cnt_black = [0] * (2 * MAX_K + 1)
cnt_white = [0] * (2 * MAX_K + 1)

black, white, grey = 0, 0, 0

# OFFSET 해주기 위함
cur = MAX_K
for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)

    if c == "L":
        # x 칸 왼쪽으로 칠하기
        while x > 0:
            a[cur] = 1
            cnt_white[cur] += 1
            x -= 1
            
            if x:
                cur -= 1

    else:
        while x > 0:
            a[cur] = 2
            cnt_black[cur] += 1
            x -= 1

            if x:
                cur += 1

for i in range(2*MAX_K+1):
    if cnt_white[i] >= 2 and cnt_black[i] >= 2:
        grey += 1
    elif a[i] == 1:
        white += 1
    elif a[i] == 2:
        black += 1

print(white,black,grey
)