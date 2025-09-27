n, m = map(int, input().split())

# Please write your code here.
arr=[[0 for _ in range(m)] for _ in range(n)]

# step 1, step 2로 나눠야 함

# step 1

count=1

for start_col in range(m):
    curr_row=0
    curr_col=start_col

    while 0 <= curr_col and curr_row < n:
        arr[curr_row][curr_col]=count

        curr_row+=1
        curr_col-=1
        count+=1

for start_row in range(1,n):
    curr_row=start_row
    curr_col=m-1

    while 0 <= curr_col and curr_row < n:
        arr[curr_row][curr_col]=count

        curr_row += 1
        curr_col -= 1
        count += 1


for row in arr:
    for col in row:
        print(col,end=' ')
    print()
    
    