n = int(input())
# n=4
# 0,1,2,3
for i in range(n):
    for _ in range(n-i):
        print("*",end="")
    for _ in range(i):
        print(" ",end="")
    for _ in range(i):
        print(" ",end="")
    for _ in range(n-i):
        print("*",end="")
    print()