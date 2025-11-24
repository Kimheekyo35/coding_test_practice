offset = 1000
max_r = 2*offset

tuple_rec = [
    tuple(map(int,input().split()))
    for _ in range (2)
]
m_rec = tuple(map(int,input().split()))

a = [
    [0] * (max_r+1)
    for _ in range(max_r+1)
]

for x1,y1,x2,y2 in tuple_rec:
    x1, y1 = x1+offset, y1+offset
    x2, y2 = x2+offset, y2+offset

    for i in range(x1,x2):
        for j in range(y1,y2):
            a[i][j] = 1

xm1,ym1 = m_rec[0]+offset,m_rec[1]+offset
xm2,ym2 = m_rec[2]+offset,m_rec[3]+offset

for i in range(xm1,xm2):
    for j in range(ym1,ym2):
        a[i][j] = 0

cnt = 0
for i in range(max_r+1):
    for j in range(max_r+1):
        if a[i][j] == 1:
            cnt += 1

print(cnt)
