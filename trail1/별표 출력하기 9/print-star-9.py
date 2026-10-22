n = int(input())
# n=3
for i in range(n):
    # i=0,1,2
    for j in range(n-i-1):
        # 2(0,1),1(0)
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
