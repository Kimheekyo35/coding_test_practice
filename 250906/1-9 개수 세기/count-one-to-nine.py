n=int(input())
arr=list(map(int,input().split()))
cnt_list=[0]*10
cnt=1
for i in arr:
    cnt_list[i]+=1

for i in range(1,len(cnt_list)):
    print(cnt_list[i])
