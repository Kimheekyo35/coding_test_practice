n, m, k = map(int, input().split())
lit = set()
ans, cnt = -1, 0

for _ in range(m):
    number = int(input())
    if number in lit:
        cnt += 1
    else:
        lit.add(number)
    if cnt >= k:
        ans = number
        break

print(ans)
