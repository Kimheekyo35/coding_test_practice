R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
cnt = 0

for i in range(1,R):
    for j in range(1,C):
        # R-1 랑 C-1로 두는 건 열의 맨마지막으로 가면, 다음 점프 못함
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
# \는 파이썬에서 여러 줄로 나누어서 적지만 한 줄로 읽히고 싶을 때 씀
                if (grid[0][0] != grid[i][j] and 
                grid [i][j] != grid[k][l] and 
                # 맨마지막 행,열과 비교
                grid[k][l] != grid[R-1][C-1] ):
                    cnt += 1
       

print(cnt)
            
        
        

