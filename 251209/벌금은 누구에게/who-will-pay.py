n, m, k = map(int, input().split())
lit = set()
ans, cnt = -1, 0

## 이 코드가 틀린 이유는 맨 처음에 들어온 것들이 cnt 0으로 찍히기 때문
for _ in range(m):
    number = int(input())
    if number in lit:
        cnt += 1
    else:
        lit.add(number)
        cnt += 1
    if cnt >= k:
        ans = number
        break

print(ans)
