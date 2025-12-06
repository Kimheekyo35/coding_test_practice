import sys
N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

stud_cnt = [0]*N
stud_rank = [0]*N
answer = -1

for s in student:
    for idx,cnt in enumerate(stud_cnt):
        if s == idx+1:
            stud_cnt[idx] += 1
        if cnt == K:
            stud_rank[idx] += 1

for rank in stud_rank:
    if rank == 1:
        answer = stud_rank.index(rank)+1
        break

print(answer)

