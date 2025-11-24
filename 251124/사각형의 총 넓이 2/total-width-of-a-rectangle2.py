OFFSET = 100
MAX_R = 2*OFFSET

n = int(input())
dir_tuple = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
# 2차원 만드는 방법
a = [
    [0]*(MAX_R+1)
    for _ in range(MAX_R+1)
]

for x1,y1,x2,y2 in dir_tuple:
    x1,y1 = x1+OFFSET, y1+OFFSET
    x2,y2 = x2+OFFSET, y2+OFFSET

    for i in range(x1,x2):
        for j in range(y1,y2):
            a[i][j] = 1

cnt = 0
for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if a[i][j] == 1:
            cnt += 1

print(cnt)
