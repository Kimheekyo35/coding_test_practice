a, b = map(int, input().split())

# Please write your code here.

def is_even(n):
    if ((n // 10) + (n % 10)) % 2 == 0:
        return True
    else:
        return False

def is_prime(n):
    if n < 2:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False

    return True

cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_even(i):
        cnt += 1

print(cnt)


