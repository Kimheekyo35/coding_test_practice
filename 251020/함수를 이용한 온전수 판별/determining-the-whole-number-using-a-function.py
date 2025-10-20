a, b = map(int, input().split())

# Please write your code here.

def is_on(n):
    if  n % 2 != 0 and n % 10 != 5 and (n % 3 != 0 or n % 9 == 0):
        return True

cnt = 0
for i in range(a,b+1):
    if is_on(i):
        cnt += 1

print(cnt)