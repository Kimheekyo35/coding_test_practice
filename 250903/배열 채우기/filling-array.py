arr=list(map(int,input().split()))


new_arr=[]
for i,k in enumerate(arr):
    if i==0 and k==0:
        pass
    elif k==0:
        break
    else:
        new_arr.append(k)

for i in new_arr[::-1]:
    print(i,end=" ")

