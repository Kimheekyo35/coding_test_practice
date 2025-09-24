n,m=tuple(map(int,input().split()))

arr1=[list(map(int,input().split())) for _ in range(n)]
arr2=[list(map(int,input().split())) for _ in range(n)]

new_list=[[0 for _ in range(len(arr1[0]))] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j]==arr2[i][j]:
            new_list[i][j]=0
        else:
            new_list[i][j]=1

for row in new_list:
    for elem in row:
        print(elem,end=' ')    
    print()
