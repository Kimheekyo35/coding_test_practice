N = int(input())

# Please write your code here.
result = 0

def mul(n):

    if n == 1:
        return 2
    if n == 2:
        return 4
    
    return (mul(n-1) * mul(n-2)) % 100

print(mul(N))