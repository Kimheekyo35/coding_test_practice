N = int(input())

# Please write your code here.

def f(n):
    if n % 2 != 0:
        if n == 1:
            return 1
        return f(n-2) + n
    else:
        if n == 2:
            return 2
        return f(n - 2) + n

print(f(N))