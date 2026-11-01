n = int(input())
cnt = 1
for _ in range(n):
    for _ in range(n):
        print(cnt*2,end=" ")
        cnt += 1
        if cnt == 5:
            cnt = 1
    print()