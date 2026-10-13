a, b = map(int,input().split())
sum_val = 0
if a>b:
    replace_num = 0
    replace_num = a # a값 저장
    a = b # b값 a에 저장
    b = replace_num

for i in range(a,b+1):
    if i%5==0:
        sum_val += i

print(sum_val)