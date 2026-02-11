A = input()

# Please write your code here.

lena = len(A)
cnt = 0
for i in range(lena-2):
    for j in range(i+2,lena-1):
        if (A[i] =="(" and A[i+1]=="(") and (A[j]==")" and A[j+1]==")"):
            cnt += 1

print(cnt)