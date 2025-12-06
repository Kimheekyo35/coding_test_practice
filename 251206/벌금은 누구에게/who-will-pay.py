N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

stud_cnt = [0]*N

for s in student:
    for idx,cnt in enumerate(stud_cnt):
        if s == idx+1:
            stud_cnt[idx] += 1
        if cnt == 3:
            break

answer = -1
for stud in stud_cnt:
    if stud == 3:
        answer = stud_cnt.index(stud)+1
        break

print(answer)



# Please write your code here.