arr=list(map(int,input().split()))

cnt_list=[0 for _ in range(7)]

for i in arr:
    cnt_list[i]+=1

for i in range(1,len(cnt_list)):
    print(f"{i} - {cnt_list[i]}")