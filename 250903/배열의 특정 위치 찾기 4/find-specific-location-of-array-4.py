list_a=list(map(int,input().split()))

cnt=0
even=0
for i in list_a:
    if i==0:
        break
    elif i>0 and i%2==0:
        even+=i
        cnt+=1
        

print(cnt,end=' ')
print(even)
