arr=list(map(str,input().split()))

for i in range(10):
    num_list=[2,5,8]
    for j in num_list:
        if i+1==j:
            print(arr[i],end=' ')