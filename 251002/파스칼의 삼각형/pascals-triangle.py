n=int(input())

arr_2d=[]
for _ in range(n):
    arr_2d.append([])


for i in range(n):
    for _ in range(i+1):
        arr_2d[i].append(1)
        
for i in range(2,n):
    for j in range(1,i):
        arr_2d[i][j]=arr_2d[i-1][j-1]+arr_2d[i-1][j]

for row in arr_2d:
    for elem in row:
        print(elem,end=' ')
    print()
