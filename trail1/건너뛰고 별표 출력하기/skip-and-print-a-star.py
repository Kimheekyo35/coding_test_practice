n = int(input())
# n=4
for i in range(1,n+1):
    # i=1,2,3,4
    for j in range(1,i+1):
        # j=1,2,3,4
        print("*",end="")
    print("\n")
# 4,3,2,1
for i in range(n,0,-1):
    for j in range(i-1):
        print("*",end="")
    print("\n")