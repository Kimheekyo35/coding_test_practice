n = int(input())
num_list = [3,6,9]
for i in range(1,n+1):
    first = i%10
    second = i//10

    if i % 3 == 0:
        print(0,end=' ')
    elif first in num_list or second in num_list:
        print(0,end=' ')
    else:
        print(i,end=' ')
    
    
    
    
    