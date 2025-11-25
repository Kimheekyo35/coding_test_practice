offset = 1000
max_r = 2*offset

map_rec = [
    [0]*(max_r+1)
    for _ in range(max_r+1)
]

rect = [tuple(map(int,input().split())) for _ in range(2)]

for i,(x1,y1,x2,y2) in enumerate(rect,start=1):
    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for row in range(x1,x2):
        for col in range(y1,y2):
            map_rec[row][col] += i

cnt_1 = 0
cnt_3 = 0

for i in range(max_r+1):
    for j in range(max_r+1):
        if map_rec[i][j] == 1:
            cnt_1 += 1
        elif map_rec[i][j] == 3:
            cnt_3 += 1

print(cnt_1+cnt_3)

