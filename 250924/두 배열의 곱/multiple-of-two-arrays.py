arr1=[[0 for _ in range(3)] for _ in range(3)]

arr2=[[0 for _ in range(3)] for _ in range (3)]

num=1
for i in range(3):
    for j in range(3):
        arr1[i][j]=num
        arr2[i][j]=arr1[i][j]+1
        print(arr1[i][j]*arr2[i][j],end=' ')
        num+=1
    print()