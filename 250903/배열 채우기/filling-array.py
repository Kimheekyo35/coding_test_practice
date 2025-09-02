arr=list(map(int,input().split()))

new_arr=[i for i in arr[::-1]]

for i,k in enumerate(new_arr):
    if i==0 and k==0:
        pass
    elif k==0:
        break
    else:
        print(k,end=' ')