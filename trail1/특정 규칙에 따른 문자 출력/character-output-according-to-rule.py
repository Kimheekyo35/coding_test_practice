n = int(input())

# 1,2
for i in range(1,n+1):
    for _ in range(n-i):
        print(" ",end=" ")
    for _ in range(i):
        print("@",end=" ")
    print()
# 2, 1
for i in range(n-1,0,-1):
    for _ in range(i):
        print("@",end=" ")
    print()