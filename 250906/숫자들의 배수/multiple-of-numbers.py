n=int(input())
arr=[0]*10

arr[0]=n

for i in range(1,10):
    arr[i]=arr[i-1]+arr[0]


cnt=0
for elem in arr:
    print(elem,end=' ')
    if elem%5==0:
        cnt+=1
    if cnt>=2:
        break