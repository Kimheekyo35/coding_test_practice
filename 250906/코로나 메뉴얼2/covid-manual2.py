heat_list=[0]*4

for _ in range(3):
    a,b =list(map(str,input().split()))
    
    if a=='Y':
        if int(b)>=37:
            heat_list[0]+=1
        else:
            heat_list[2]+=1
    else:
        if int(b)>=37:
            heat_list[1]+=1
        else:
            heat_list[3]+=1

for i in heat_list:
    print(i,end=' ')

if heat_list[0]>=2:
    print('E')


    


