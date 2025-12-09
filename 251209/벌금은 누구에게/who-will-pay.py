n, m, k = map(int, input().split())
count = {}          # number별 등장 횟수 저장
ans = -1

for _ in range(m):
    number = int(input())
    
    # number 등장 횟수 1 증가
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

    # 이 number가 처음으로 k번 이상 등장했다면 정답
    if count[number] >= k:
        ans = number
        break

print(ans)
