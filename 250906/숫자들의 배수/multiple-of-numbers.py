n=int(input())

cnt=0
for i in range(1,11):
    k=i*n
    if k%5==0:
        cnt+=1
    if cnt==2:
        print(k)
        break
    print(k,end=' ')
