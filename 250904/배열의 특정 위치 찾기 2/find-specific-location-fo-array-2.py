arr=list(map(int,input().split()))

sum_even=0
sum_odd=0
for i in range(len(arr)):
    if i%2==0:
        sum_even+=arr[i]
    else:
        sum_odd+=arr[i]

if sum_even>sum_odd:
    print(sum_even-sum_odd)
else:
    print(sum_odd-sum_even)