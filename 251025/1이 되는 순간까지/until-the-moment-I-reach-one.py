N = int(input())

# Please write your code here.
# cnt = 0

# def div(n):
#     global cnt
#     if n == 1:
#         return cnt
#     if n % 2 == 0:
#         cnt += 1
#         n //= 2
#         return div(n)
#     else:
#         cnt += 1
#         n //= 3
#         return div(n)

# print(div(N))

def get_num(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return get_num(n) + 1
    else:
        return get_num(n) + 1

print(get_num(N))