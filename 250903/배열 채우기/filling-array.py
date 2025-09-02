arr=list(map(int,input().split()))


for i in arr[::-1]:
    if i==0:
        break
    else:
        print(i,end=' ')