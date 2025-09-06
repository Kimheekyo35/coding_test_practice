arr=list(map(int,input().split()))

for i in arr:
    if i==0:
        break
    if i%2==0:
        i=i//2
    else:
        i=i+3
    print(i,end=' ')