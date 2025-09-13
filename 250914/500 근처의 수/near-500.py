arr=list(map(int,input().split()))


under_500_list=[i for i in arr if i<500]
over_500_list=[i for i in arr if i>500]


max_val=under_500_list[0]
for i in under_500_list:
    if max_val<i:
        max_val=i

min_val=over_500_list[0]
for i in over_500_list:
    if min_val>i:
        min_val=i


print(max_val, min_val)
# print(max(under_500_list), min(over_500_list))
    