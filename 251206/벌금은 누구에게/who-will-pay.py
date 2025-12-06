import sys
N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

stud_cnt = [0]*(N+1)

answer = -1
for score in student:
    stud_cnt[score] += 1
    if stud_cnt[score] >= K:
        answer = stud_cnt.index(K)
        break

print(answer)

