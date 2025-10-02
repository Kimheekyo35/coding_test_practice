n,m = tuple(map(int,input().split()))

# input_rc = [list(map(int,input().split())) for _ in range(m)]

arr_2d = [ 
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r,c = tuple(map(int,input().split()))
    
    arr_2d[r-1][c-1] = 1

for elem in arr_2d:
    print(*elem)