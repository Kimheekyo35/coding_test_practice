dirs = input()
x, y = 0, 0
# 동남서북 기준
dxs, dys = [1,0,-1,0],[0,-1,0,1]
# 북에서 시작하니까 curr_dirs => 3
curr_dir = 3
flag = False
leng = len(dirs)
time_at = 0

for i in range(leng):
    time_at += 1
    c_dir = dirs[i]
    # 3 -> 2 -> 1 -> 0
    if c_dir == "L":
        curr_dir = (curr_dir+3)%4
    # 3 -> 0 -> 1->2
    elif c_dir == "R":
        curr_dir = (curr_dir+1)%4
    else:
        x, y = x+dxs[curr_dir], y+dys[curr_dir]
    if x == 0 and y == 0:
        flag = True
        break

if flag:
    print(time_at)
else:
    print(time_at)