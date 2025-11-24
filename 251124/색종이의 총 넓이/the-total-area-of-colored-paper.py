n = int(input())
offset = 100
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
a = [
    [0]*(2*offset+1)
    for _ in range(2*offset+1)
]

for x1,y1 in points:
    x1,y1 = x1+offset, y1+offset

    for i in range(x1,x1+8):
        for j in range(y1,y1+8):
            a[i][j] = 1

cnt = 0
for i in range(2*offset+1):
    for j in range(2*offset+1):
        if a[i][j] == 1:
            cnt += 1
print(cnt)