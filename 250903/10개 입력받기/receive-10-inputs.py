list_a=list(map(int,input().split()))

cnt=0
for i in list_a:
    if i==0:
        break
    cnt+=1

sum_i=0
for i in range(0,cnt):
    sum_i+=list_a[i]

        
        
print(sum_i, f"{(sum_i/cnt):.1f}")
