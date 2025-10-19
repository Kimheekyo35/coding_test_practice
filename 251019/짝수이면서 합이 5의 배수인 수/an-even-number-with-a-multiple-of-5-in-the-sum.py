n = int(input())

# Please write your code here.

def choose_num(n):
    sum_num = (n % 10) + (n // 10)
    return n % 2 == 0 and sum_num % 5 == 0

def print_num(n):
    if choose_num(n):
        print("Yes")
    else:
        print("No")

print_num(n)