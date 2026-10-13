n = int(input())
sum_val = 0

for _ in range(n):
    input_num = int(input())
    
    if input_num%2 and input_num%3==0:
        sum_val += input_num

print(sum_val)