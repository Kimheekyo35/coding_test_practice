
num_list=list(map(int,input().split()))

new_list=[]

for n in num_list:
    if n>=250:
        break
    else:
        new_list.append(n)

sum_i=0
for i in new_list:
    sum_i+=i
    avg=(sum_i/len(new_list))

print(sum_i,avg)
    


