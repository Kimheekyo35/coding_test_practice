n, m = tuple(map(int,input().split()))
time_a, time_b = 1, 1

offset = 1000
max_r = 2*offset

list_a, list_b = [0]*(max_r+1), [0]*(max_r+1)
# 첫 번째
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        list_a[time_a] = list_a[time_a-1] + (1 if d == "R" else -1) 
        time_a += 1


for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        list_b[time_b] = list_b[time_b-1] + (1 if d == "R" else -1)
        time_b += 1

ans = -1
for i in range(1,time_a):
    if list_a[i] == list_b[i]:
        ans = i
        break

print(ans)