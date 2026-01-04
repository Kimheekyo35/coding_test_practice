n = int(input())
way_tuple = [tuple(input().split()) for _ in range(n)]

x, y = 0, 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for way in way_tuple:
    if way[0] == 'N':
        y += dy[1] * int(way[1])
    elif way[0] == 'E':
        x += dx[0] * int(way[1])
    elif way[0] == 'S':
        y += dy[3] * int(way[1])
    else:
        x += dx[2] * int(way[1])

    
print(x,y)
# Please write your code here.