n=int(input())

cnt=0
for _ in range(n):
    sum_arr=0
    arr=list(map(int,input().split()))

    sum_arr=sum(arr)

    if (sum_arr/len(arr))>=60:
        print("pass")
        cnt+=1
    else:
        print("fail")

print(cnt)

        
