n = int(input())
S = input()

# Please write your code here.
C_cnt = 0
O_cnt = 0
W_cnt = 0
for i in S:
    if i == "C":
        C_cnt += 1
    elif i == "O":
        O_cnt += 1
    else:
        W_cnt += 1

print(C_cnt*O_cnt*W_cnt)
        