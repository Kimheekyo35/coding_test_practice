n,q=tuple(map(int,input().split()))

arr=list(map(int,input().split()))


for _ in range(q):
    ques_list=tuple(map(int,input().split()))

    if ques_list[0]==1:
        index_num=ques_list[1]
        print(arr[index_num-1])
    
    elif ques_list[0]==2:
        idx=-1
        if ques_list[1] in arr:
            idx=arr.index(ques_list[1])
        print(idx+1)

    else:
        for elem in range(ques_list[1]-1,ques_list[2]):
            print(arr[elem],end=' ')
        print()
            
