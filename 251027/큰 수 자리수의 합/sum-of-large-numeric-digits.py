a, b, c = map(int, input().split())

# Please write your code here.

def mul_func():
    return str(a*b*c)


sum_val = 0

def num_plus(n):
    total_val = mul_func()
    global sum_val

    if n == 0:
        return

    sum_val += int(total_val[n-1])
    return num_plus(n-1)

num_plus(len(mul_func()))
print(sum_val)
