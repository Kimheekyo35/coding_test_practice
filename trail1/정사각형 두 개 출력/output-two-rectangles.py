n = int(input())
cnt = 0

while cnt < 2:
    for _ in range(n):
        for _ in range(n):
            print("*",end="")
        print()
    print()
    cnt += 1