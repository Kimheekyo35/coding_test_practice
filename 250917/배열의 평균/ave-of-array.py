arr_2d=[list(map(int,input().split())) for _ in range(2)]

sum_row=[sum(arr_2d[i])/4 for i in range(2)]

sum_col=[]
for j in range(4):
    sum_col_1=((arr_2d[0][j]+arr_2d[1][j])/2)
    sum_col.append(sum_col_1)

total=0
for i in range(2):
    for j in range(4):
        total+=arr_2d[i][j]

total_val=[(total/(2*4))]

result=[]
result.append((sum_row,sum_col,total_val))

for i in range(len(result)):
    for j in range(len(result[i])):
        for elem in result[i][j]:
            print(f"{elem:.1f}",end=' ')
        print()