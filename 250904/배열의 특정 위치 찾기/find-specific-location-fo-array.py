arr=list(map(int,input().split()))

sum_i=0
new_list=[]

for i,k in enumerate(arr):
    j=i+1
    if j%2==0:
        sum_i+=k
    if j%3==0 and j!=1:
        new_list.append(arr[i])
        avg=sum(new_list)/len(new_list)


print(sum_i,avg)
