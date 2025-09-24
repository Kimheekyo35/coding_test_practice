arr=list(map(int,input().split()))
n=arr[0]
m=arr[1]

new_list=[[0 for _ in range(m)] for _ in range(n)]
num=1
for i in range(n):
    for j in range(m):
        new_list[i][j]=num
        print(num,end=' ')
        num+=1
        
    print()
        