n,q=tuple(map(int,input().split()))

arr=list(map(int,input().split()))

for _ in range(q):
    ques=list(map(int,input().split()))
    
    if ques[0]==1:
        print(arr[(ques[1])-1])
    elif ques[0]==2:
        idx=-1
        if ques[1] in arr:
            idx=arr.index(ques[1])
        
        print(idx+1)
    else:
        for i in range(ques[1]-1,ques[2]):
            print(arr[i],end=' ')
        print()

        
    