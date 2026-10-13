a, b = map(int,input().split())
sum_val = 0
count_num = 0

for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sum_val += i
        count_num += 1

# 소수점 첫째자리까지 -> round함수
avg = round(sum_val/count_num,1)
print(sum_val,avg)
