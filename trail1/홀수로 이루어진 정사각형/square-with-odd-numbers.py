n = int(input())
k = 11

for i in range(n):
    tmp = k
    for j in range(n):
        print(tmp,end=" ")
        tmp += 2
    k += 2

    print()
