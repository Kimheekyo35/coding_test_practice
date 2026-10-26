n = int(input())
# n = 1
# i = 0, 1, 2
for i in range(2*n+1):
    for j in range(2*n+1):
        if j % 2 == 0 or i % 2 == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()