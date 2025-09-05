arr=list(map(int,input().split()))


p=arr[1]
pp=arr[0]
for _ in range(3,11):
    pp,p=p,pp+p
    if p and pp not in arr:
        arr.append(pp)
        arr.append(p)

for i in arr:
    print(i%10,end=' ')