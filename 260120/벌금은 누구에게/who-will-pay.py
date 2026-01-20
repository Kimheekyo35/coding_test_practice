n,m,k = tuple(map(int,input().split()))
num_list = [0]*(n+1)
cnt = 0

for _ in range(m):
    number = int(input())
    num_list[number] += 1

cnt = -1
for i in num_list:
    if i == k: cnt = num_list.index(k)

if cnt==-1: print(cnt)
else: print(cnt)
