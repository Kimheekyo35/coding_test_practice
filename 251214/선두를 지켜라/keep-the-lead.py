n, m = map(int, input().split())

limit = 1000000
# Process A's movements
a_list = [0] * (limit)
b_list = [0] * (limit)

a_status = 1
va, vat = 0, 0
for _ in range(n):
    v,t = tuple(map(int,input().split()))
    
    for i in range(a_status,a_status+t):
        a_list[i] += a_list[i-1] + v
        a_status += 1

b_status = 1
vb,vbt = 0, 0
for _ in range(m):
    v, t = tuple(map(int,input().split()))

    for i in range(b_status,b_status+t):
        b_list[i] += b_list[i-1] + v
        b_status += 1
    
cnt = 0

for i in range(1,a_status):
    if (a_list[i]==b_list[i]) and (a_list[i+1]-b_list[i+1] != 0):
        cnt += 1

print(cnt)