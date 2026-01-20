n = int(input())
x,y = 0, 0
dx, dy = [1,0,-1,0], [0,-1,0,1]

for _ in range(n):
    way, how = input().split()
    if way == 'N':
        x+=dx[3]
        y+=dy[3]*int(how)
    elif way == 'S':
        x+=dx[1]
        y+=dy[1]*int(how)
    elif way == 'E':
        x+=dx[0]*int(how)
        y+=dy[0]
    else:
        x+=dx[2]*int(how)
        y+=dy[2]

print(x,y)
    