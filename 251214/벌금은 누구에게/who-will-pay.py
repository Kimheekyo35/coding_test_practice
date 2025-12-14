n, m, k = tuple(map(int, input().split()))

count_list = [0] * (m+1)
answer = -1
for _ in range(m):
    num = int(input())
    count_list[num] += 1

    if count_list[num] >= k:
        answer = num
        break

print(answer)