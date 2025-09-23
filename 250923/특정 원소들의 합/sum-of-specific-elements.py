total_arr=[]
for _ in range(4):
    arr=list(map(int,input().split()))
    total_arr.append(arr)

total=0
for i in range(4):
    for j in range(4):
        if j<=i:
            total+=total_arr[i][j]
print(total)