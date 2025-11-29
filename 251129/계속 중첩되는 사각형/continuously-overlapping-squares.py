n = int(input())

offset = 100
max_r = 2*offset

# 1은 빨강, 2는 파랑

rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

checked = [
    [0]*(max_r+1)
    for _ in range(max_r+1)
]

for i, (x1,y1,x2,y2) in enumerate(rects,start=1):
    x1 += offset
    x2 += offset
    y1 += offset
    y2 += offset

    for x in range(x1,x2):
        for y in range(y1,y2):
            if i % 2 != 0:
                checked[x][y] = 1
            else:
                checked[x][y] = 2
cnt = 0
for i in range(max_r+1):
    for j in range(max_r+1):
        if checked[i][j] == 2:
            cnt += 1

print(cnt)