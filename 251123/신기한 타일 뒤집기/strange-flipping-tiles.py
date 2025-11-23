n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
max_k = 200000

origin = [0] * (max_k+1)
cur = 100000
black,white = 0,0

for num, direction in commands:
    num = int(num)
    if direction == "L":
        while cur > cur-num:
            cur -= 1
            origin[cur] = 1
        cur = cur - num + 1
        print(cur)
    else:
        while cur < cur+num:
            cur += 1
            # origin[cur] = 2
        cur = cur + num - 1
        print(cur)
for i in range(max_k+1):
    if origin[i] == 1: white += 1
    elif origin[i] == 2: black += 1

print(white,black)
