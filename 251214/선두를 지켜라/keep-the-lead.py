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
    
leader, ans = 0, 0
for i in range(1,a_status):
    if a_list[i] > b_list[i]:
        # 기존 리더가 b인데 a가 더 큰거니까
        if leader == 2:
            ans += 1
        # 리더를 a로 갱신
        leader = 1
    
    elif a_list[i] < b_list[i]:
        if leader == 1:
            ans += 1
        leader = 2

print(ans)
