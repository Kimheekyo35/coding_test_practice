n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

for i in range(1,len(a)):
    for j in range(0,i):
        if a[i]>a[j]:
            a[j],a[i]=a[i],a[j]
    
    

print(a[0],a[1])