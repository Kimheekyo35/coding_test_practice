n=int(input())

arr=[[0 for i in range(n)] for j in range(n)]

num=1
for i in range(n):
    for j in range(n):
        arr[i][j]=num
        num+=1

for j in range(n):
    for i in range(n):
        print(arr[i][j],end=' ')
    print()

