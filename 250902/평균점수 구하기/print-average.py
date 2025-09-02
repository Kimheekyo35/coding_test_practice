point_list=list(map(float,input().split()))

avg=0
sum_p=0
for p in point_list:
    sum_p+=p
    avg=sum_p/len(point_list)

print(avg)