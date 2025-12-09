n, m = tuple(map(int,input().split()))
num = 2000000
A_status = 1
A_list = [0]*(num+1)

b_status = 1
b_list = [0]*(num+1)

for _ in range(n):
    way, step = input().split()
    step = int(step)
    for _ in range(step):
        if way == 'R':
            A_list[A_status] = A_list[A_status-1] + 1
        else:
            A_list[A_status] = A_list[A_status-1] - 1
        A_status += 1

for _ in range(m):
    way, step = input().split()
    step = int(step)
    for _ in range(step):
        if way == "R":
            b_list[b_status] = b_list[b_status-1] + 1
        else:
            b_list[b_status] = b_list[b_status-1] - 1
        b_status += 1

answer = -1
for i in range(1,A_status):
    if A_list[i] == b_list[i]:
        answer = i
        break

print(answer)