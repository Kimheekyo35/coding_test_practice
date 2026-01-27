N = int(input())
moves = [tuple(input().split()) for _ in range(N)]

dx, dy = [0,-1,0,1],[1,0,-1,0]
time_at = 0
sx, sy = 0, 0

def loc(a,b):
    return a == 0 and b == 0
        

def find_loc(a, b, how, way,time_at):
    for _ in range(how):
        a += dx[way]
        b += dy[way]
        time_at += 1
        if loc(a,b):
            return a,b,time_at
    return a,b,time_at

def find_0_0():
    global sx, sy
    time_at = 0

    for i in range(N):
        dir = moves[i][0]
        how = int(moves[i][1])

        if dir == "N":
            sx,sy,time_at = find_loc(sx,sy,how,0,time_at)
            
        elif dir == "S":
            sx,sy,time_at = find_loc(sx,sy,how,2,time_at)
        
        elif dir == "E":
            sx,sy,time_at = find_loc(sx,sy,how,1,time_at)

        else:
            sx,sy,time_at = find_loc(sx,sy,how,3,time_at)

        if sx == 0 and sy == 0:
            return(time_at)

if find_0_0():
    print(find_0_0())
else:
    print(-1)






        


