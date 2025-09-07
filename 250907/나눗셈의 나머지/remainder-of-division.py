a,b=list(map(int,input().split()))
arr=[0]*(b)

c=0
while a!=0:
    c=a%b
    a=a//b
    arr[c]+=1
    if a==0:
        break

sum_ele=0
for ele in arr:
    sum_ele+=(ele**2)

print(sum_ele)
