n,m,k = tuple(map(int,input().split()))
num_list = [0]*(n+1)
cnt = -1

for _ in range(m):
    number = int(input())
    num_list[number] += 1
    if num_list[number] == k:
        cnt = num_list.index(k)
        break
    
if cnt==-1: print(cnt)
else: print(cnt)
