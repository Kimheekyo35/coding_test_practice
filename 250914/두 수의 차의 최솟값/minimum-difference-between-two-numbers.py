
n=int(input())

arr=list(map(int,input().split()))

min_result=100
for i in range(n):
    for j in range(i+1,n):
        result=arr[j]-arr[i]
        if min_result>result:
            min_result=result

print(min_result)

        