arr=list(map(int,input().split()))
cnt_list=[0 for _ in range(len(arr))]

for i in arr:
    if i==0:
        break
    i=i//10
    cnt_list[i]+=1

for i in range(1,len(cnt_list)):
    print(f"{i} - {cnt_list[i]}")
