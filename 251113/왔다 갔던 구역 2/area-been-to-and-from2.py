n = int(input())

answer = []
left_length = 0
right_length = 0

for _ in range(n):
    xi,yi = tuple(input().split())
    xi = int(xi)
    answer.append((xi,yi))
    if yi == "R":
        right_length += xi
    else:
        left_length -= xi

lines = [0 for _ in range(left_length,right_length)]
check_lines = [i for i in range(left_length,right_length)]
status = 0
for step, way in answer:
    if way == "R":
        for i in range(status,status+step):
            lines[i] += 1
        status += step
    # 빼기 범위 헷갈림..
    else:
        for i in range(status-1,status-step-1,-1):
            lines[i] += 1
        status -= step

count = 0
for i in lines:
    if i >= 2:
        count += 1


print(count)
