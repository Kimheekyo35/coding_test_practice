n = int(input())

for i in range(2*n):
    # 1,3,5
    if i%2:
        for _ in range(1+i//2):
            print("*",end=" ")
        print()
    # 0,2,4
    else:
        for _ in range(n-i//2):
            print("*",end=" ")
        print()