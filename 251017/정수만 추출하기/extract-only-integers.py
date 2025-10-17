a,b = input().split()

sum_num = 0
sum_str = ""

for i in range(0,len(a)):
    if a[i].isdigit():
        sum_str += a[i]
    else:
        sum_num += int(sum_str)
        sum_str = ""
        break

for j in range(0,len(b)):
    if b[j].isdigit():
        sum_str += b[j]
    else:
        sum_num += int(sum_str)
        break
    
print(sum_num)

