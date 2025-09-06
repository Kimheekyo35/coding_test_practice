arr=list(map(int,input().split()))

score_list=[0 for _ in range(11)]

for i in arr:
    if i==0:
        break
    i=i//10
    score_list[i]+=1

for i in range(10,0,-1):
    print(f"{i*10} - {score_list[i]}")

