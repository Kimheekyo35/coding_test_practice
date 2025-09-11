n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

min_num=sys.maxsize
for num in a:
    if min_num>num:
        min_num=num

cnt=0
for num in a:
    if min_num==num:
        cnt+=1

print(min_num,cnt)