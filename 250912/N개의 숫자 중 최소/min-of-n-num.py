n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

cnt=1
min_num=sys.maxsize
for num in a:
    if min_num>num:
        min_num=num
        cnt=1


    elif min_num==num:
        cnt+=1

print(min_num,cnt)

# print(min_num)

# min_val=a[0]
# count=1

# for i in range(1,n):
#     if min_val>a[i]:
#         min_val=a[i]
#         #초기화되니까 cnt는 1부터 시작
#         cnt=1
#     elif min_val==a[i]:
#         cnt+=1

# print(min_val,cnt)