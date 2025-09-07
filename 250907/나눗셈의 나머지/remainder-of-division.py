a,b=list(map(int,input().split()))
arr=[0]*(b)

c=0
while a!=0:
    a=a//b
    c=a%b
    arr[c]+=1
    if a==0:
        break

sum_ele=0
for ele in arr:
    sum_ele+=(ele*ele)

print(sum_ele)
