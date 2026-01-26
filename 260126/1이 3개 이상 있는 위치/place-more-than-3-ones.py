n = int(input())

num_squ = [
    list(map(int,input().split())) for _ in range(n)
]

def loc(a,b):
    return a>=0 and a<4 and b>=0 and b<4

dxs, dys = [0,1,0,-1],[1,0,-1,0]

def find_1(a,b):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = a+dx, b+dy
        if loc(nx,ny) and num_squ[nx][ny]==1:
            cnt += 1
        if cnt == 3:
            return cnt
            

total = 0
for i in range(n):
    for j in range(n):
        if find_1(i,j):
            total += 1

print(total)




