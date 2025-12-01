max_t = 1000000

# 변수 선언 및 입력
n, m = tuple(map(int,input().split()))
# a와 b의 리스트를 따로따로 만들어줌
pos_a, pos_b = [0]*(max_t+1), [0]*(max_t+1)

time_a = 1
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        # pos_a[현재위치] = pos_a[이전위치] + (1 if d == .....)
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b-1] + (1 if d == "R" else -1)
        time_b += 1

# 최초로 만나는 시간 구하기
ans = -1
for i in range(1,time_a):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)


