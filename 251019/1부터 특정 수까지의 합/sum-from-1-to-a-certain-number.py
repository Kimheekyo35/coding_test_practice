n = int(input())

# Please write your code here.

def sum_num(n):
    result = 0
    for i in range(1,n+1):
        result += i

    return result//10

print(sum_num(n))