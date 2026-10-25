n = int(input())
first = 1
second = n
for i in range(1,2*n+1):
    # 1,3,5
    if i%2:
        for _ in range(first):
            print("*",end=" ")
        print()
        first += 1
    # 2,4,6
    else:
        for _ in range(second,0,-1):
            print("*",end=" ")
        print()
        second -= 1