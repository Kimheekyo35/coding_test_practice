n = int(input())

arr_2d =  [[1 for _ in range(n)] for _ in range(n)]

for row in range(1,n):
    for col in range(1,n):
        arr_2d[row][col] = arr_2d[row-1][col] + arr_2d[row][col-1] + arr_2d[row-1][col-1]

for elem in arr_2d:
    print(*elem)