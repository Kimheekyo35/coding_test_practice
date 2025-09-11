arr=list(map(int,input().split()))

max_num=0
for a in arr:
    if a>max_num:
        max_num=a

print(max_num)