n,q=tuple(map(int,input().split()))

arr=list(map(int,input().split()))


for _ in range(q):
    n_list=list(map(int,input().split()))
    
    qq=n_list[0]

    if qq==1:
        print(arr[(n_list[1]-1)])
    elif qq==2:
        a=n_list[1]
        idx=-1
        if a in arr:
            idx=arr.index(a)
        print(idx+1)
    else:
        for i in range((n_list[1]-1),n_list[2]):
            print(arr[i],end=' ')
        print(" ")
        
    