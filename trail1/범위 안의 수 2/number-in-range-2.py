sum_val = 0
count_num = 0
for _ in range(10):
    n = int(input())
    if 0<=n<=200:
        sum_val += n
        count_num += 1

print(sum_val,round(sum_val/count_num,1))