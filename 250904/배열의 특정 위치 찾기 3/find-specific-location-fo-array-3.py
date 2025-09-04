arr=list(map(int,input().split()))


new_list=[]
for i in arr:
    if i==0:
        break
    new_list.append(i)

print(new_list[-1]+new_list[-2]+new_list[-3])