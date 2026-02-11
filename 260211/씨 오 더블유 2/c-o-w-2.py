n = int(input())
S = input()

# Please write your code here.
cnt = 0

for i in range(len(S)):
    for j in range(i+1,len(S)):
        for k in range(j+1,len(S)):
            if (S[i]=="C" and S[j]=="O" and S[k]=="W"):
                cnt += 1

print(cnt)       