n =int(input())
# 2,1
for i in range(n,0,-1):
    # 0,1
    for _ in range(n-i):
        print(" ",end=" ")
    for _ in range(2*i-1):
        print("*",end=" ")
    print()
# 1,2
for i in range(1,n):
    for _ in range(n-i-1):
        print(" ",end=" ")
    for _ in range(2*i+1):
        print("*",end=" ")
    print()
        
        