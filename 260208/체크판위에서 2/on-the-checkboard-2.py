R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
cnt = 0
status = grid[0][0]
for i in range(R-1):
    for j in range(C-1):
        if status != grid[i+1][j+1]:
            status = grid[i+1][j+1]
            cnt += 1
            break

print(cnt-1)
            
        
        

