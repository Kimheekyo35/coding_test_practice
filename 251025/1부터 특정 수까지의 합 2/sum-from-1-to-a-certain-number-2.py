N = int(input())

# Please write your code here.

def sum_start(n):
    if n == 1:
        return 1
    return sum_start(n-1) + n

print(sum_start(N))