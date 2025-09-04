arr=list(map(int,input().split()))


sum_i=0
new_list=[]
for i in range(len(arr)):
    if (i+1)%2!=0:
        sum_i+=arr[i+1]
    if (i+1)%3==0:
        new_list.append(arr[i])
        avg=sum(new_list)/len(new_list)

print(sum_i,f"{avg:.1f}")

    