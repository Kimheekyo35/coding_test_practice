ab_list = list(map(str,input().split()))

sum_num = 0
sum_str = ""
a = ab_list[0]
b = ab_list[1]
k = 0
while True:
    if k == 0:
        for i in range(0,len(a)):
            if a[i].isdigit():
                sum_str += a[i]
            else:
                
                break
        sum_num += int(sum_str)
        sum_str = ""
    else:
        for j in range(0,len(b)):
            if b[j].isdigit():
                sum_str += b[j]
            else:
                break
        sum_num += int(sum_str)
    k += 1
    
    if k > 1:
        break
    
        
print(sum_num)

