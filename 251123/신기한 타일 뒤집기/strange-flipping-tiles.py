n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
max_k = 200000

origin = [0] * (max_k+1)
cur = 100000
black, white = 0, 0

for num, direction in commands:
    num = int(num)
    if direction == "L":
        for _ in range(num):
            origin[cur] = 1
            cur -=1
        cur += 1
    else:
        for _ in range(num):
            origin[cur] = 2
            cur += 1
        cur -= 1

for i in range(max_k+1):
    if origin[i] == 1: white += 1
    elif origin[i] == 2: black += 1

print(white,black)
