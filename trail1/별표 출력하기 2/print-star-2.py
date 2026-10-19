n = int(input())


# for j in range(n,0,-1):
#     print("* "*j)
    
# n = 5, n = 4, n = 3, n = 2, n = 1

for i in range(n): # 0, 1, 2, 3, 4
    for _ in range(n-i): # 5, 4, 3, 2, 1
        print("*",end=" ")
    print()

