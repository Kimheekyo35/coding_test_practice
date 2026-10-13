n = int(input())
sum_val = 0

for _ in range(n):
    input_num = int(input())
    
    # input_num%2 -> True
    # input_num%3==0 -> 3의 배수
    if input_num%2 and input_num%3==0:
        sum_val += input_num

print(sum_val)