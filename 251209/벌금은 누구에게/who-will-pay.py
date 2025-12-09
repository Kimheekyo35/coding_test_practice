n, m, k = tuple(map(int,input().split()))
lit = []
ans, cnt = -1, 0
for _ in range(m):
    number = int(input())
    if number in lit:
        cnt += 1
    else:
        lit.append(number)
    if cnt == k:
        ans = k
        break

print(ans)
